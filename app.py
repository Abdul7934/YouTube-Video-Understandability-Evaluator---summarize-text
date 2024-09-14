from utils.data_collection import get_transcript
from utils.preprocessing import preprocess_text
from utils.feature_extraction import get_tfidf_features
from utils.content_analysis import compute_similarity, analyze_sentiment
from utils.evaluation import compute_understanding_score
from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarizer pipeline
summarizer = pipeline("summarization")

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be" in url:
        return url.split('/')[-1].split('?')[0]
    else:
        return url

def summarize_text(text):
    """Summarize the given text using a pre-trained model."""
    # Ensure that the text is not too short for summarization
    if len(text.split()) < 50:  # If the text is too short
        return text  # Return the text as is (no summarization)
    
    # Summarize the text with min 15 lines and max 4 paragraphs (adjust lengths)
    try:
        summary = summarizer(text, max_length=400, min_length=150, do_sample=False)
        return summary[0]['summary_text'] if summary else "No summary available"
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Error during summarization"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        links = request.form['links'].splitlines()  # Split input links by newlines
        
        summaries = []
        cleaned_texts = []
        
        # Process each video
        for link in links:
            video_id = extract_video_id(link)
            transcript = get_transcript(video_id)
            
            # Check if transcript retrieval was successful
            if not transcript:
                summaries.append("Transcript not available")
                cleaned_texts.append("")  # Append empty string to keep list lengths consistent
                continue
            
            cleaned_text = preprocess_text(transcript)
            
            # Avoid empty or very short text
            if len(cleaned_text) < 20:
                summaries.append("Insufficient content for summarization")
                cleaned_texts.append("")  # Append empty string to keep list lengths consistent
                continue
            
            # Summarize the cleaned transcript
            summary = summarize_text(cleaned_text)
            summaries.append(summary)
            cleaned_texts.append(cleaned_text)

        # Ensure we have data to analyze
        if not cleaned_texts:
            return render_template('index.html', error="No valid transcripts found", subject=subject)

        # Feature Extraction
        try:
            tfidf_matrix, _ = get_tfidf_features(cleaned_texts)
        except Exception as e:
            return render_template('index.html', error=f"Error in feature extraction: {e}", subject=subject)

        # Content Analysis (similarity and sentiment)
        try:
            similarity_matrix = compute_similarity(tfidf_matrix)
            sentiment_scores = [analyze_sentiment(text) for text in cleaned_texts]
        except Exception as e:
            return render_template('index.html', error=f"Error in content analysis: {e}", subject=subject)

        # Ensure that the length of scores matches the number of texts
        if len(cleaned_texts) != len(sentiment_scores) or len(sentiment_scores) != len(similarity_matrix):
            return render_template('index.html', error="Mismatch in data lengths", subject=subject)

        # Evaluation & Ranking
        try:
            scores = [compute_understanding_score(similarity_matrix[i][i], sentiment_scores[i]) for i in range(len(cleaned_texts))]
        except Exception as e:
            return render_template('index.html', error=f"Error calculating scores: {e}", subject=subject)

        # Check if scores list is empty before accessing index
        if not scores:
            return render_template('index.html', error="Error calculating scores", subject=subject)

        best_video_index = scores.index(max(scores)) if scores else None
        best_video = links[best_video_index] if best_video_index is not None and best_video_index < len(links) else None
        best_summary = summaries[best_video_index] if best_video_index is not None and best_video_index < len(summaries) else None

        return render_template('index.html', best_video=best_video, best_summary=best_summary, subject=subject)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
