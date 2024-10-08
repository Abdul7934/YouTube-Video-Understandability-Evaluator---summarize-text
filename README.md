4.Divide and Conquer
 
Merge sort
##########
1.Merging two sorted arrays
def merge_and_sort(arr1, arr2):
   # Get the lengths of the arrays
   n = len(arr1)
   m = len(arr2)
 
   # Initialize pointers for both arrays and the combined array
   i = 0
   j = 0
   combined_array = []
 
   # Merge the arrays using two pointers
   while i < n and j < m:
       if arr1[i] < arr2[j]:
           combined_array.append(arr1[i])
           i += 1
       else:
           combined_array.append(arr2[j])
           j += 1
 
   # Add remaining elements from arr1
   while i < n:
       combined_array.append(arr1[i])
       i += 1
 
   # Add remaining elements from arr2
   while j < m:
       combined_array.append(arr2[j])
       j += 1
 
   return combined_array
 
# Input sizes and arrays
size1 = int(input())
arr1 = list(map(int, input().split()))
 
size2 = int(input())
arr2 = list(map(int, input().split()))
 
# Call the function and print the result
result = merge_and_sort(arr1, arr2)
print(*result)
 
2.Merge sort algorithm
# Replace '_' to solve the problem
 
def Merge(a, size_a, b, size_b, c):
   idx1 = 0
   idx2 = 0
   idx = 0
 
   while idx1 < size_a and idx2 < size_b:
       if a[idx1] < b[idx2]:
           c[idx] = a[idx1]
           idx1 += 1
       else:
           c[idx] = b[idx2]
           idx2 += 1
       idx += 1
 
   while idx1 < size_a:
       c[idx] = a[idx1]
       idx1 += 1
       idx += 1
 
   while idx2 < size_b:
       c[idx] = b[idx2]
       idx2 += 1
       idx += 1
 
def Sort(a, size_a):
   if size_a <= 1:
       return
 
   mid = size_a//2
 
   sz1 = mid
   sz2 = size_a - mid
 
   a1 = [0] * sz1
   a2 = [0] * sz2
 
   for i in range(mid):
       a1[i] = a[i]
 
   for i in range(mid ,size_a ):
       a2[i-mid] = a[i]
 
   Sort(a1, sz1)
   Sort(a2, sz2)
 
   Merge(a1, sz1, a2, sz2 , a )
 
if __name__ == "__main__":
   n = int(input())
   a = list(map(int , input().split()))
 
   Sort(a, n)
 
   for i in range(n):
       print(a[i], end=" ")
   print()
 
3.Inversion Count
 
# cook your dish here
MOD = 10**9 + 7
 
def merge(a, size_a, b, size_b, c):
   idx1, idx2, idx = 0, 0, 0
 
   while idx1 < size_a and idx2 < size_b:
       if a[idx1] < b[idx2]:
           c[idx] = a[idx1]
           idx1 += 1
       else:
           c[idx] = b[idx2]
           idx2 += 1
       idx += 1
 
   while idx1 < size_a:
       c[idx] = a[idx1]
       idx1 += 1
       idx += 1
 
   while idx2 < size_b:
       c[idx] = b[idx2]
       idx2 += 1
       idx += 1
 
def count_inversions(a, size_a, b, size_b):
   ptr = size_b - 1
   ans = 0
   for i in range(size_a):
       while ptr >= 0 and b[ptr] < a[i]:
           ptr -= 1
       ans = (ans + (size_b - 1 - ptr)) % MOD
   return ans
 
def sort_and_count(a, size_a):
   if size_a < 2:
       return 0
 
   mid = size_a // 2
 
   a1 = a[:mid]
   a2 = a[mid:]
 
   sz1 = len(a1)
   sz2 = len(a2)
 
 
   left = sort_and_count(a1, sz1)
   right = sort_and_count(a2, sz2)
 
   num = count_inversions(a1, sz1, a2, sz2)
 
 
   merged = [0] * size_a
   merge(a1, sz1, a2, sz2, merged)
 
   for i in range(size_a):
       a[i] = merged[i]
 
   return ((left + right) % MOD + num) % MOD
 
 
t = int(input())
 
for _ in range(t):
   n = int(input())
   a = list(map(int, input().split()))
 
   print(sort_and_count(a, n))
 
 
Quick sort
##########
 
1.Partitioning the array
# Replace '_' to solve the problem
def partition(a, size_a):
   pivot = a[size_a-1]
   idx = 0
 
   for i in range(size_a):
       if a[i] <= pivot:
           a[idx], a[i] = a[i], a[idx]
           idx += 1
 
   a[idx], a[size_a - 1] = a[size_a - 1], a[idx]
 
 
if __name__ == "__main__":
   n = int(input())
 
   a = list(map(int, input().split()))
 
   partition(a, n)
 
   for i in range(n):
       print(a[i], end=" ")
 
   print()
 
2.Implementing quick sort
def partition(a, l, r):
   """
   Partition the array into two parts and return the index of the pivot element.
   Args:
   - a: The array to be partitioned
   - l: The leftmost index of the subarray
   - r: The rightmost index of the subarray
   Returns:
   - The index of the pivot element
   """
   pivot = a[r]
   idx = l
 
   for i in range(l, r):
       if a[i] <= pivot:
           a[idx], a[i] = a[i], a[idx]
           idx += 1
 
   a[idx], a[r] = a[r], a[idx]
 
   # Return the final pivot index
   return idx
 
 
def sort(a, l, r):
   """
   Recursive function to sort the array using quicksort.
   Args:
   - a: The array to be sorted
   - l: The leftmost index of the subarray
   - r: The rightmost index of the subarray
   """
   if r - l < 1:
       return  # Arrays of size 1 and 0 are already sorted
 
   pivot = partition(a, l, r)
 
   # Sorting both halves of the array
   sort(a, l, pivot - 1)
   sort(a, pivot + 1, r)
 
 
if __name__ == "__main__":
   n = int(input())
 
   a = list(map(int, input().split()))
 
   sort(a, 0, n - 1)
 
   for i in range(n):
       print(a[i], end=" ")
 
   print()
 
3.Randomised Quick Sort
import random
 
def partition(a, l, r):
   """
   Partition the array into two parts and return the index of the pivot element.
   Args:
   - a: The array to be partitioned
   - l: The leftmost index of the subarray
   - r: The rightmost index of the subarray
   Returns:
   - The index of the pivot element
   """
   pivot = a[r]
   idx = l
 
   for i in range(l, r):
       if a[i] <= pivot:
           a[idx], a[i] = a[i], a[idx]
           idx += 1
 
   a[idx], a[r] = a[r], a[idx]
 
   # Return the final pivot index
   return idx
 
def random_part(a, l, r):
   """
   Swap a random element with the last element in the subarray.
   Args:
   - a: The array
   - l: The leftmost index of the subarray
   - r: The rightmost index of the subarray
   """
   rand_idx = random.randint(l, r)
   a[rand_idx], a[r] = a[r], a[rand_idx]
 
def sort(a, l, r):
   """
   Recursive function to sort the array using quicksort.
   Args:
   - a: The array to be sorted
   - l: The leftmost index of the subarray
   - r: The rightmost index of the subarray
   """
   if r - l < 1:
       return  # Arrays of size 1 and 0 are already sorted
 
   random_part(a, l, r)
   pivot = partition(a, l, r)
 
   # Sorting both halves of the array
   sort(a, l, pivot - 1)
   sort(a, pivot + 1, r)
 
if __name__ == "__main__":
   n = int(input())
 
   a = list(map(int, input().split()))
 
   sort(a, 0, n - 1)
 
   for i in range(n):
       print(a[i], end=" ")
 
   print()
 
 
Binary search
#############
 
1.Sequential Search
def search(arr, x, n):
   # Write your code here
   for i in range(n):
       if arr[i] == x:
           return i+1
   
   return -1
 
if __name__ == "__main__":
   t = int(input())
 
   for _ in range(t):
       n, x = map(int, input().split())
       arr = list(map(int, input().split()))
 
       result = search(arr, x, n)
       print(result)
 
2.Binary Search
# Replace '_' to solve the problem
def binary_search(arr, target):
   left = 0
   right = len(arr)-1
 
   while right >= left:
       mid = (left + right) // 2
       if arr[mid] == target:
           return mid + 1
       elif arr[mid] > target:
           right = mid-1
       else:
           left = mid+1
 
   return -1
 
if __name__ == "__main__":
   t = int(input())
   
   while t > 0:
       n, x = map(int, input().split())
       arr = list(map(int, input().split()))
 
       result = binary_search(arr, x)
       print(result)
 
       t -= 1
 
3.Average Flex
 
# cook your dish here
 
 
def upperbound(a , key):
   left =0
   right = len(a)
   
   while( right > left ):
       
       mid = (right+left)//2
       
       if( a[mid] <= key ):
           
           left = mid +1
           
       else :
           right = mid
           
           
   return left
           
 
 
t = int(input())
 
for _ in range(t):
   n = int(input())
   a = list( map( int , input().split()))
   a.sort()
   count =0
   for i in range(n):
       index = upperbound(a,a[i])
       if( index > n-index  ):
           count = count+1
           
   print(count)
   
       
 
 
Multiplication of large integers
################################
 
1.Divide and Conquer Multiplication
 
 
# Input the number of test cases
t = int(input())
 
# Process each test case
for _ in range(t):
   # Input numbers as strings
   num1 = int(input())
   num2 = int(input())
 
   result = num1*num2
 
   print(result)
 
2.Optimised Divide and Conquer
import java.util.Scanner;
 
public class Main {
   // Pad the numbers with 0 to make their sizes equal
   static void makeEqualSize(StringBuilder A, StringBuilder B) {
       while (A.length() < B.length()) {
           A.insert(0, '0');
       }
       while (B.length() < A.length()) {
           B.insert(0, '0');
       }
   }
 
   // Digit subtraction of the numbers
   static String subtract(String A, String B) {
       StringBuilder C, D;
       C = new StringBuilder(A);
       D = new StringBuilder(B);
       makeEqualSize(C, D);
       A = C.toString();
       B = D.toString();
 
       boolean sign = false;
       if (A.compareTo(B) < 0) {
           sign = true;
           String temp = A;
           A = B;
           B = temp;
       }
       int borrow = 0;
       StringBuilder res = new StringBuilder();
       for (int i = A.length() - 1; i >= 0; i--) {
           int dA = (A.charAt(i) - '0') - borrow;
           int dB = (B.charAt(i) - '0');
 
           if (dA < dB) {
               dA += 10;
               borrow = 1;
           } else {
               borrow = 0;
           }
 
           int digit = (dA - dB) % 10;
           char d = (char) (digit + '0');
           res.insert(0, d);
       }
       if (sign) {
           res.insert(0, '-');
       }
       return res.toString();
   }
 
   // Digit addition of the numbers
   static String add(String A, String B) {
       if (A.length() > 0 && A.charAt(0) == '-') {
           return subtract(B, A);
       }
       if (B.length() > 0 && B.charAt(0) == '-') {
           return subtract(A, B);
       }
 
       StringBuilder C, D;
       C = new StringBuilder(A);
       D = new StringBuilder(B);
       makeEqualSize(C, D);
       A = C.toString();
       B = D.toString();
 
       int carry = 0;
       StringBuilder res = new StringBuilder();
       for (int i = A.length() - 1; i >= 0; i--) {
           int sum = (A.charAt(i) - '0') + (B.charAt(i) - '0') + carry;
           int digit = sum % 10;
           carry = sum / 10;
           char d = (char) (digit + '0');
           res.insert(0, d);
       }
       if (carry != 0) {
           char d = (char) (carry + '0');
           res.insert(0, d);
       }
       return res.toString();
   }
 
   // Remove extra leading zeroes
   static String removeLeadingZeros(String S) {
       boolean f = true;
       StringBuilder res = new StringBuilder();
       for (char c : S.toCharArray()) {
           if (f && c == '0') {
               continue;
           }
           f = false;
           res.append(c);
       }
       return res.toString();
   }
 
   // Multiply the number with powers of 10
   static String multiplyTenPower(String S, int power) {
       S = removeLeadingZeros(S);
       StringBuilder result = new StringBuilder(S);
       while (power-- > 0) {
           result.append('0');
       }
       return result.toString();
   }
 
   // Function to multiply the numbers
   static String multiply(String A, String B) {
       if (A.length() < B.length()) {
           String temp = A;
           A = B;
           B = temp;
       }
 
       StringBuilder C, D;
       C = new StringBuilder(A);
       D = new StringBuilder(B);
       makeEqualSize(C, D);
       A = C.toString();
       B = D.toString();
 
 
       int N = A.length();
 
       if (N == 1) { // Base case
           int res = (A.charAt(0) - '0') * (B.charAt(0) - '0');
           return Integer.toString(res);
       }
 
       // Pad one extra 0 to make the length even
       if ((N & 1) == 1) {
           N++;
           A = "0" + A;
           B = "0" + B;
       }
 
       int firstHalfSize = N - N / 2;
       int secondHalfSize = N / 2;
 
       // Distribute into two halves
       StringBuilder a1 = new StringBuilder();
       StringBuilder a2 = new StringBuilder();
       StringBuilder b1 = new StringBuilder();
       StringBuilder b2 = new StringBuilder();
 
       for (int i = 0; i < firstHalfSize; i++) {
           a1.append(A.charAt(i));
           b1.append(B.charAt(i));
       }
 
       for (int i = firstHalfSize; i < N; i++) {
           a2.append(A.charAt(i));
           b2.append(B.charAt(i));
       }
 
       String A1 = a1.toString();
       String B1 = b1.toString();
       String A2 = a2.toString();
       String B2 = b2.toString();
 
       // Take all the smaller multiplications
       String W = multiply(A1, B1);
       String X = multiply(A2, B2);
       String Y = multiply(add(A1, A2), add(B1, B2));
 
       // Store the answer
       String ans = add(add(multiplyTenPower(W, N), multiplyTenPower(subtract(Y, add(W, X)), N / 2)), X);
 
       // // Return the answer with no leading zeros
       return removeLeadingZeros(ans);
   }
 
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       int t = scanner.nextInt();
       scanner.nextLine();
       while (t-- > 0) {
           String num1 = scanner.nextLine();
           String num2 = scanner.nextLine();
 
           System.out.println(multiply(num1, num2));
       }
   }
}
 
 
​​​​​​​​5.Greedy techniques
 
 
 
Basics of Greedy, and proofs
############################
 
1.Chef and String
def max_pairs(s):
   count = 0
   i = 0
   while i < len(s) - 1:
       if (s[i] == 'x' and s[i + 1] == 'y') or (s[i] == 'y' and s[i + 1] == 'x'):
           count += 1
           i += 2  # Move past this pair
       else:
           i += 1  # Move to the next character
   return count
 
# Read the number of test cases
T = int(input())
for _ in range(T):
   S = input().strip()
   print(max_pairs(S))
 
 
Job scheduling problem
######################
 
1.Job Scheduling problem
# cook your dish here
 
import heapq
 
class Job:
   def __init__(self, id, t, d):
       self.id = id
       self.t = t
       self.d = d
 
   def __lt__(self, other):
       return self.d < other.d
 
def maxfun(joblist):
   pq = []
   for job in joblist:
       heapq.heappush(pq, job)
   
   order = []
   currtime = 0
   maxlate = 0
 
   while pq:
       curr = heapq.heappop(pq)
       currtime += curr.t
       order.append(curr.id)
       
       late = max(0, currtime - curr.d)
       maxlate = max(late, maxlate)
 
   print(maxlate)
 
   print(" ".join(map(str, order)))
 
 
t = int(input())
 
joblist = []
for i in range(t):
   time, dead = map(int, input().split())
   job = Job(i + 1, time, dead)
   joblist.append(job)
 
maxfun(joblist)
 
Prim's Algorithm
################
 
1.Implementation of Prims
N = 10
vis = [False] * N
adj = [[] for _ in range(N)]
MST = []
 
class Pair:
   def __init__(self, first, second):
       self.first = first
       self.second = second
 
def prims(source, n):
   global MST, vis
 
   # Stores weight, newly added vertex, and parent vertex
   pq = []
 
   def push_to_pq(item):
       pq.append(item)
       pq.sort()
 
   push_to_pq((0, source))  # push the starting vertex to the pq
 
   while pq:
       node = pq.pop(0)
 
       v = node[1]
 
       # If vertex is already processed, continue
       if vis[v]:
           continue
 
       vis[v] = True  # Mark vertex as processed
 
       print(f"Adding vertex {v} to the MST")
 
       if len(node) == 3:
           MST.append(Pair(node[2], v))  # Push the edge into the MST
 
       for edge in adj[v]:
           push_to_pq((edge.second, edge.first, v))
 
   print("\nEdgelist of MST is:")
 
   for edge in MST:
       print(edge.first, edge.second)
 
if __name__ == "__main__":
   for i in range(N):
       vis.append(False)
       adj.append([])
 
   # Adjacency list
   adj[1].append(Pair(2, 4))
   adj[2].append(Pair(1, 4))
 
   adj[1].append(Pair(3, 4))
   adj[3].append(Pair(1, 4))
 
   adj[2].append(Pair(3, 2))
   adj[3].append(Pair(2, 2))
 
   adj[3].append(Pair(4, 3))
   adj[4].append(Pair(3, 3))
 
   adj[3].append(Pair(5, 2))
   adj[5].append(Pair(3, 2))
 
   adj[3].append(Pair(6, 4))
   adj[6].append(Pair(3, 4))
 
   adj[4].append(Pair(6, 3))
   adj[6].append(Pair(4, 3))
 
   adj[5].append(Pair(6, 3))
   adj[6].append(Pair(5, 3))
 
   prims(1, 6)
 
2.Calculate MST weight
import java.util.*;
 
class main {
 
   static final int N = 200010;
   static ArrayList<Boolean> vis = new ArrayList<>(N);
   static ArrayList<ArrayList<Pair>> adj = new ArrayList<>(N);
 
   static ArrayList<Pair> MST = new ArrayList<>(); // Stores the edge list of the Minimum Spanning Tree
 
   static class Pair {
       int first, second;
 
       Pair(int first, int second) {
           this.first = first;
           this.second = second;
       }
   }
 
   static void prims(int source, int n) { // Source is the starting vertex
       long ans = 0;
       // Write your solution here
       
       PriorityQueue<int[]> pq = new PriorityQueue<>( (a,b) -> Integer.compare(a[0],b[0]) );
       
       pq.add( new int[]{0,source} );
       
 
       
       while( pq.size() != 0 )
       {
           
           int[] node = pq.poll();
           
           int v = node[1];
           
           if( vis.get(v) )
           {
               continue;
           }
           
           vis.set(v, true);
           
           if(node.length ==3)
           {
               ans = ans + node[0];
           }
           
           for(Pair edge : adj.get(v) )
           {
               pq.add(new int[] { edge.second, edge.first , v  }  );
           }
           
           
           
       }
       
       
       
       
 
 
       System.out.println(ans);
   }
 
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
 
       for (int i = 0; i < N; i++) {
           vis.add(false);
           adj.add(new ArrayList<>());
       }
 
       int n = scanner.nextInt();
       int m = scanner.nextInt();
 
       for (int i = 0; i <= n; i++) {
           adj.set(i, new ArrayList<>());
       }
 
       for (int i = 0; i < m; i++) {
           int x = scanner.nextInt();
           int y = scanner.nextInt();
           int w = scanner.nextInt();
           adj.get(x).add(new Pair(y, w));
           adj.get(y).add(new Pair(x, w));
       }
 
       prims(1, n);
   }
}
 
3.Road Decoration
# cook your dish here
import heapq
 
class UnionFind:
   def __init__(self, size):
       self.parent = [i for i in range(size)]
 
   def find(self, u):
       if u != self.parent[u]:
           self.parent[u] = self.find(self.parent[u])
       return self.parent[u]
 
   def union(self, u, v):
       u = self.find(u)
       v = self.find(v)
       if u != v:
           self.parent[u] = v
 
def main():
   t = int(input())
   for _ in range(t):
       graph = {}
       edgeList = []
       n, m = map(int, input().split())
       for i in range(n):
           graph[i] = []
       for _ in range(m):
           u, v, w = map(int, input().split())
           graph[u].append((v, w))
           graph[v].append((u, w))
           edgeList.append((u, v, w))
       edgeList.sort(key=lambda x: x[2])
 
       uf = UnionFind(n)
       mst = 0
       cnt = 0
 
       for edge in edgeList:
           u, v, w = edge
           if uf.find(u) == uf.find(v):
               continue
           else:
               uf.union(u, v)
               mst += w
               cnt += 1
 
       if cnt != n - 1:
           print("NO")
           continue
 
       dist = [float('inf')] * n
       edgeChosen = [0] * n
       dist[0] = 0
       pq = [(0, 0)]
 
       while pq:
           d, u = heapq.heappop(pq)
           if dist[u] < d:
               continue
           for v, w in graph[u]:
               if dist[v] > w + d:
                   dist[v] = w + d
                   heapq.heappush(pq, (w + d, v))
                   edgeChosen[v] = w
               elif dist[v] == w + d and w < edgeChosen[v]:
                   edgeChosen[v] = w
 
       mdt = sum(edgeChosen)
       if mdt == mst:
           print("YES")
       else:
           print("NO")
 
if __name__ == "__main__":
   main()
 
Huffman Trees and codes
#######################
 
1.Implementing Huffman Algorithm
import heapq
from collections import defaultdict
 
class Node:
   def __init__(self, data, frequency):
       self.data = data
       self.frequency = frequency
       self.left = None
       self.right = None
 
   # Define comparison operators for nodes
   def __lt__(self, other):
       return self.frequency < other.frequency
 
def build(s):
   frequency_map = defaultdict(int)
   for char in s:
       frequency_map[char] += 1
 
   min_heap = [Node(char, frequency) for char, frequency in frequency_map.items()]
   heapq.heapify(min_heap)
 
   while len(min_heap) > 1:
       node1 = heapq.heappop(min_heap)
       node2 = heapq.heappop(min_heap)
 
       internal_node = Node('$', node1.frequency + node2.frequency)
       internal_node.left = node1
       internal_node.right = node2
 
       heapq.heappush(min_heap, internal_node)
 
   return min_heap[0]
 
def generate_codes(root, code, codes):
   if root:
       if root.data != '$':
           codes[root.data] = code
       generate_codes(root.left, code + '0', codes)
       generate_codes(root.right, code + '1', codes)
 
def dictionary(root):
   codes = {}
   generate_codes(root, '', codes)
 
 
def encode(s):
   codes = {}
   generate_codes(build(s), '', codes)
 
   encoded = ''.join(codes[char] for char in s)
   return encoded
 
def decode(encoded, root):
   current = root
   decoded = ""
 
   for bit in encoded:
       if bit == '0':
           current = current.left
       else:
           current = current.right
 
       if current.left is None and current.right is None:
           decoded += current.data
           current = root
 
   return decoded
 
if __name__ == "__main__":
   s = "Hello! This message will be encoded"
 
   root = build(s)
   dictionary(root)
 
   encoded = encode(s)
   # print("The encoded string is:", encoded)
   decoded = decode(encoded, root)
   print("The decoded string is:", decoded)
 
​​​​​​​​6.Dynamic programming
 
 
Knapsack problem
################
 
1.Fractional Knapsack Problem
def main():
   import sys
   input = sys.stdin.read
   data = input().split()
 
   n = int(data[0])
   wmax = float(data[1])
 
   items = []
   index = 2
   for _ in range(n):
       w = float(data[index])
       v = float(data[index + 1])
       value_per_weight = v / w  
       items.append((value_per_weight, w))
       index += 2
 
   items.sort(reverse=True, key=lambda x: x[0])
 
   ans = 0
   for value_per_weight, weight in items:
       if wmax <= 0:
           break
       weight_to_take = min(wmax, weight)
       ans += weight_to_take * value_per_weight
       wmax -= weight_to_take
 
   print(f"{ans:.16f}")
 
if __name__ == "__main__":
   main()
 
2.Knapsack Problem
def knapsack(N, W_max, weights, values):
   dp = [[0] * (W_max + 1) for _ in range(N + 1)]
 
   for i in range(1, N + 1):
       for w in range(W_max + 1):
           dp[i][w] = dp[i-1][w]  
           if w >= weights[i-1]:
               dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
 
   return dp[N][W_max]
 
def main():
   import sys
   input = sys.stdin.read
   data = input().split()
 
   N = int(data[0])
   W_max = int(data[1])
 
   weights = []
   values = []
 
   index = 2
   for _ in range(N):
       weights.append(int(data[index]))
       values.append(int(data[index + 1]))
       index += 2
 
   print(knapsack(N, W_max, weights, values))
 
if __name__ == "__main__":
   main()
 
3.Subset Sum Problem
def can_form_subset(A, X):
   # DP array to store if a sum j is possible
   dp = [False] * (X + 1)
   dp[0] = True  # Base case: sum of 0 is always possible
 
   # Process each element in the array
   for num in A:
       # Update the DP table in reverse to prevent overwriting
       for j in range(X, num - 1, -1):
           if dp[j - num]:
               dp[j] = True
 
   # Result is whether we can form the sum X
   return dp[X]
 
def main():
   import sys
   input = sys.stdin.read
   data = input().split()
   
   N = int(data[0])
   X = int(data[1])
   A = list(map(int, data[2:2+N]))
 
   if can_form_subset(A, X):
       print("YES")
   else:
       print("NO")
 
if __name__ == "__main__":
   main()
 
Longest common subsequence
##########################
 
1.Longest Common Subsequence
import java.util.*;
 
public class Main {
   public static void main(String[] args) {
       // Write your code here
       Scanner sc = new Scanner(System.in);
       
       String a = sc.next();
       String b = sc.next();
       
       int m = a.length();
       int n = b.length();
       
       int [][] dp = new int[m+1][n+1];
       
       for(int i =0 ; i< m+1; i++ )
       {
           for(int j =0 ; j< n+1 ; j++ )
           {
               dp[i][j] = -1;
           }
       }
       
       System.out.println( LCS(a,b,m,n,dp) );
 
   }
   
   public static int LCS( String a , String b , int m , int n , int[][] dp )
   {
       
       
       
       if( m == 0 || n == 0 )
       {
           return 0;
       }
       
       
       if( dp[m][n] != -1 )
       {
           return dp[m][n];
       }
       
       if( a.charAt(m-1) == b.charAt(n-1) )
       {
           dp[m][n] = 1+ LCS(a,b,m-1,n-1,dp);
           return dp[m][n];
       }
       
       dp[m][n] = Math.max( LCS(a,b,m,n-1,dp) , LCS(a,b,m-1,n,dp)  );
       
       return dp[m][n];
       
   }
}
 
2.Longest Palindromic Subsequence
import java.util.Scanner;
 
public class Main {
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       
       // Reading input
       String S = scanner.nextLine();
       int n = S.length();
       
       // Call the function to find the length of the longest palindromic subsequence
       int result = longestPalindromicSubsequence(S, n);
       
       // Output the result
       System.out.println(result);
       
       scanner.close();
   }
   
   public static int longestPalindromicSubsequence(String S, int n) {
       // Create a 2D DP array
       int[][] dp = new int[n][n];
       
       // Every single character is a palindrome of length 1
       for (int i = 0; i < n; i++) {
           dp[i][i] = 1;
       }
       
       // Fill the DP table
       for (int length = 2; length <= n; length++) {
           for (int i = 0; i < n - length + 1; i++) {
               int j = i + length - 1;
               
               if (S.charAt(i) == S.charAt(j)) {
                   dp[i][j] = dp[i + 1][j - 1] + 2;
               } else {
                   dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
               }
           }
       }
       
       // Result is the length of the longest palindromic subsequence in the entire string
       return dp[0][n - 1];
   }
}
 
Warshall and Floyd Algorithm
############################
 
1.All to All Shortest Path
def floyd_warshall(N, edges):
   INF = float('inf')
   
   dist = [[INF] * N for _ in range(N)]
 
   for u, v, w in edges:
       dist[u][v] = min(dist[u][v], w)
       dist[v][u] = min(dist[v][u], w)
   
 
   for k in range(N):
       for i in range(N):
           for j in range(N):
               if dist[i][k] < INF and dist[k][j] < INF:
                   dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
   
   result = []
   for i in range(N):
       row = []
       for j in range(N):
           if i == j:
               m = min(dist[i])
               if m == INF:
                   row.append('-1')
               else:
                   row.append(str(m * 2))
           else:
               if dist[i][j] == INF:
                   row.append('-1')
               else:
                   row.append(str(dist[i][j]))
       result.append(' '.join(row))
   
   return result
 
import sys
input = sys.stdin.read
data = input().split()
 
index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1
 
edges = []
for _ in range(M):
   u = int(data[index]) - 1
   index += 1
   v = int(data[index]) - 1
   index += 1
   w = int(data[index])
   index += 1
   edges.append((u, v, w))
 
results = floyd_warshall(N, edges)
for line in results:
   print(line)
 
Optimal Binary Search Trees
###########################
 
1.Optimal Binary Search Trees
import java.util.Scanner;
 
public class Main {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
 
       int N = sc.nextInt();
       int[] F = new int[N];
       for (int i = 0; i < N; i++) {
           F[i] = sc.nextInt();
       }
 
       System.out.println(optimalBST(F, N));
   }
 
   public static int optimalBST(int[] F, int N) {
       int[][] cost = new int[N][N];
       int[] freqSum = new int[N];
 
       for (int i = 0; i < N; i++) {
           freqSum[i] = F[i] + (i > 0 ? freqSum[i - 1] : 0);
       }
 
       for (int i = 0; i < N; i++) {
           cost[i][i] = F[i];
       }
 
     
       for (int len = 2; len <= N; len++) {
           for (int i = 0; i <= N - len; i++) {
               int j = i + len - 1;
               cost[i][j] = Integer.MAX_VALUE;
 
               for (int r = i; r <= j; r++) {
                   int leftCost = (r > i) ? cost[i][r - 1] : 0;
                   int rightCost = (r < j) ? cost[r + 1][j] : 0;
                   int totalCost = leftCost + rightCost + sumFrequencies(freqSum, i, j);
 
                   cost[i][j] = Math.min(cost[i][j], totalCost);
               }
           }
       }
 
       return cost[0][N - 1];
   }
 
   public static int sumFrequencies(int[] freqSum, int i, int j) {
       return freqSum[j] - (i > 0 ? freqSum[i - 1] : 0);
   }
}
 
 
 
​​​​​​​​7.Backtracking
 
n-Queens problem
################
 
1.N Queens - Backtracking
import java.util.Arrays;
 
class main {
 
   // Directions to check if queens attack another
   static int[] dx = {0, 0, -1, -1, -1, 1, 1, 1};
   static int[] dy = {-1, 1, 0, -1, 1, 0, -1, 1};
 
   static boolean check(char[][] board, int n, int row, int col) {
       for (int k = 0; k < 8; k++) {
           int x = row, y = col;
           while (x >= 0 && x < n && y >= 0 && y < n) {
               if (board[x][y] == 'Q') {
                   return false; // Queen attacks another
               }
               x += dx[k];
               y += dy[k];
           }
       }
       return true; // Can place queen here
   }
 
   static void backtrack(int row, int n, char[][] board) {
       if (row == n) { // No more rows to fill
           for (char[] x : board) { // Print the solution
               System.out.println(new String(x));
           }
           System.out.println();
           return;
       }
       for (int col = 0; col < n; col++) {
           if (check(board, n, row, col)) {
               board[row][col] = 'Q'; // Add the queen
               backtrack(row + 1, n, board);
               board[row][col] = '.'; // Remove the queen
           }
       }
   }
 
   public static void main(String[] args) {
       int n = 5;
       char[][] board = new char[n][n]; // Initialise an empty board
       for (char[] row : board) {
           Arrays.fill(row, '.');
       }
       backtrack(0, n, board);
   }
}
 
2.N Queens
def is_safe(board, row, col, n):
   # Check if there is a queen in the same column
   for i in range(row):
       if board[i][col] == 'Q':
           return False
 
   # Check if there is a queen in the left diagonal
   for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
       if board[i][j] == 'Q':
           return False
 
   # Check if there is a queen in the right diagonal
   for i, j in zip(range(row, -1, -1), range(col, n)):
       if board[i][j] == 'Q':
           return False
 
   return True
 
def solve_n_queens_util(board, row, n, result):
   if row == n:
       result.append([''.join(row) for row in board])
       return
 
   for col in range(n):
       if is_safe(board, row, col, n):
           board[row][col] = 'Q'
           solve_n_queens_util(board, row + 1, n, result)
           board[row][col] = '.'  # Backtrack
 
def solve_n_queens(n):
   board = [['.' for _ in range(n)] for _ in range(n)]
   result = []
   solve_n_queens_util(board, 0, n, result)
   return result
 
if __name__ == "__main__":
   n = int(input())
   solutions = solve_n_queens(n)
   solutions.reverse()
   for solution in solutions:
       print("\n".join(solution))
       print()
 
Hamiltonian Circuit Problem
###########################
 
1.Satisfying the Constraints
import java.util.*;
 
class main {
 
   // Check if 'next' vertex can be added after vertex 'v'
   static boolean check(int v, int next, ArrayList<Integer> circuit, boolean[][] mat) {
       // Write your code here
       
       if( !mat[v][next ] || circuit.indexOf(next)!=-1 )
       {
           return false;
       }
 
       return true;
   }
 
   static void backtrack(int v, int n, ArrayList<Integer> circuit, ArrayList<ArrayList<Integer>> ans, boolean[][] mat) {
       if (circuit.size() == n) { // Circuit is completed
           if (mat[circuit.get(0)][v]) { // Check if cycle is completed, starting should be adjacent to ending
               circuit.add(circuit.get(0));
               ans.add(new ArrayList<>(circuit));
               circuit.remove(circuit.size() - 1);
           }
           return;
       }
 
       for (int i = 1; i <= n; i++) {
           // Calling the check function
           if (!check(v, i, circuit, mat))
               continue;
 
           // If not visit and is adjacent, add it to our candidate solution
           circuit.add(i);
           backtrack(i, n, circuit, ans, mat);
           circuit.remove(circuit.size() - 1);
       }
   }
 
   // Number of vertices and adjacency matrix
   static ArrayList<ArrayList<Integer>> hamiltonianCircuit(int n, boolean[][] mat) {
       ArrayList<Integer> circuit = new ArrayList<>(); // Initially empty circuit
       ArrayList<ArrayList<Integer>> ans = new ArrayList<>(); // To store all the circuits
 
       for (int i = 1; i <= n; i++) { // Fix the starting vertex
           circuit.add(i); // Add i to circuit
           backtrack(i, n, circuit, ans, mat);
           circuit.remove(circuit.size() - 1); // Remove i from circuit
       }
 
       return ans;
   }
 
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       int n = scanner.nextInt();
       int m = scanner.nextInt();
 
       // Adjacency matrix
       boolean[][] mat = new boolean[n + 1][n + 1];
       while (m-- > 0) {
           int a = scanner.nextInt();
           int b = scanner.nextInt();
           mat[a][b] = true;
           mat[b][a] = true;
       }
       ArrayList<ArrayList<Integer>> cycles = hamiltonianCircuit(n, mat);
       cycles.sort((x, y) -> {
           return x.toString().compareTo(y.toString());
       });
 
       for (ArrayList<Integer> x : cycles) {
           for (int y : x) {
               System.out.print(y + " ");
           }
           System.out.println();
       }
   }
}
 
2.Hamiltonian Circuit
def check(v, next_v, circuit, mat):
   # Check if 'next' vertex can be added after vertex 'v'
   if not mat[v][next_v] or next_v in circuit:
       return False
   return True
 
def backtrack(v, n, circuit, ans, mat):
   if len(circuit) == n:  # Circuit is completed
       if mat[circuit[0]][v]:  # Check if cycle is completed
           circuit.append(circuit[0])  # Add the starting vertex to complete the cycle
           ans.append(list(circuit))   # Store the cycle
           circuit.pop()  # Remove the added start vertex to explore other paths
       return
 
   for i in range(1, n + 1):
       if not check(v, i, circuit, mat):
           continue
       # If adjacent and not visited, add it to the circuit
       circuit.append(i)
       backtrack(i, n, circuit, ans, mat)
       circuit.pop()  # Backtrack to explore other options
 
def hamiltonian_circuit(n, mat):
   circuit = []  # Initially empty circuit
   ans = []  # To store all valid circuits
 
   for i in range(1, n + 1):  # Fix the starting vertex
       circuit.append(i)  # Add i to the circuit
       backtrack(i, n, circuit, ans, mat)
       circuit.pop()  # Remove i from the circuit
 
   return ans
 
if __name__ == "__main__":
   # Input for number of vertices and edges
   n, m = map(int, input().split())
 
   # Adjacency matrix
   mat = [[False] * (n + 1) for _ in range(n + 1)]
   for _ in range(m):
       a, b = map(int, input().split())
       mat[a][b] = True
       mat[b][a] = True
 
   cycles = hamiltonian_circuit(n, mat)
 
   # Sorting cycles lexicographically
   cycles.sort(key=lambda x: str(x))
 
   # Output the Hamiltonian cycles
   for cycle in cycles:
       print(" ".join(map(str, cycle)))
 
Subset Sum Problem
##################
 
1.Backtracking Solution
def backtrack(idx, a, x, subset, ans):
   if idx == len(a):
       # Write your code here
       
       if( sum(subset) == x ):
           ans.append(subset[:])
 
       return
 
   backtrack(idx + 1, a, x, subset, ans)  # Don't take the i-th integer
 
   subset.append(a[idx])
   backtrack(idx + 1, a, x, subset, ans)  # Take the i-th integer
   subset.pop()
 
def subset_sum(a, x):
   subset = []  # Creating an empty subset
   ans = []  # To store all the subsets
 
   backtrack(0, a, x, subset, ans)
 
   return ans
 
if __name__ == "__main__":
   n, x = map(int, input().split())
   a = list(map(int, input().split()))
 
   subsets = subset_sum(a, x)
   subsets = [sorted(subset) for subset in subsets]
   subsets.sort()
 
   for subset in subsets:
       print(*subset)
 
2.Subset sum problem
def backtrack(idx, a, x, subset, ans):
   if idx == len(a):
       # Write your code here
       
       if( sum(subset) == x ):
           ans.append(subset[:])
 
       return
 
   backtrack(idx + 1, a, x, subset, ans)  # Don't take the i-th integer
 
   subset.append(a[idx])
   backtrack(idx + 1, a, x, subset, ans)  # Take the i-th integer
   subset.pop()
 
def subset_sum(a, x):
   subset = []  # Creating an empty subset
   ans = []  # To store all the subsets
 
   backtrack(0, a, x, subset, ans)
 
   return ans
 
if __name__ == "__main__":
   n, x = map(int, input().split())
   a = list(map(int, input().split()))
 
   subsets = subset_sum(a, x)
   subsets = [sorted(subset) for subset in subsets]
   subsets.sort()
 
   for subset in subsets:
       print(*subset)
 
3.Backtracking - Find Unique Permutations
from itertools import permutations
 
def unique_permutations(arr):
   perm = set(permutations(arr))
   return sorted(perm)
 
 
T = int(input())
 
for _ in range(T):
   N = int(input())
   arr = list(map(int, input().split()))
   
   result = unique_permutations(arr)
   
   print(len(result))
   
   for perm in result:
       print(" ".join(map(str, perm)))
 
4.Backtracking - Find Valid Parenthesis
def generate_parentheses(n):
   result = []
   
   def backtrack(s='', left=0, right=0):
       if len(s) == 2 * n:
           result.append(s)
           return
       if left < n:
           backtrack(s + '(', left + 1, right)
       if right < left:
           backtrack(s + ')', left, right + 1)
   
   backtrack()
   return sorted(result)
 
 
T = int(input())
 
for _ in range(T):
   N = int(input())
   result = generate_parentheses(N)
   
   print(len(result))
   for s in result:
       print(s)
 
5.Backtracking - Palindrome Partitioning
def is_palindrome(s):
   return s == s[::-1]
 
def find_partitions(s, start, current_partition, result):
   if start == len(s):
       result.append(current_partition[:])
       return
   for i in range(start, len(s)):
       substring = s[start:i+1]
       if is_palindrome(substring):
           current_partition.append(substring)
           find_partitions(s, i+1, current_partition, result)
           current_partition.pop()
 
def palindrome_partitions(s):
   result = []
   find_partitions(s, 0, [], result)
   result.sort()
   return result
 
 
T = int(input())
for _ in range(T):
   s = input().strip()
   partitions = palindrome_partitions(s)
   
   print(len(partitions))
   for partition in partitions:
       print(" ".join(partition))
Extra codes
def max_chopstick_pairs(N, D, L):
   # Sort the sticks in non-decreasing order of their lengths
   L.sort()
 
   pairs = 0
 
   i = 0
   while i < N - 1:
       for j in range(i + 1, N):
           if L[j] - L[i] <= D:
               pairs += 1
               L.pop(i)
               L.pop(j - 1)
               N -= 2
               i -= 1
               break
       i += 1
 
   return pairs
 
# Read input
N, D = map(int, input().split())
L = [int(input()) for _ in range(N)]
 
# Find the maximum number of usable pairs
max_pairs = max_chopstick_pairs(N, D, L)
 
print(max_pairs)
 
 
determine_winter
def determine_winner(test_cases):  
   results = []  
   for case in test_cases:  
       count_snakes = case.count('s')  
       count_mongooses = case.count('m')  
       n = len(case)  
       
       eaten = [False] * n  # To keep track of which snakes have been eaten  
       
       for i in range(n):  
           if case[i] == 'm':  
               # Try to eat the left snake if it exists and is not already eaten  
               if i > 0 and case[i - 1] == 's' and not eaten[i - 1]:  
                   eaten[i - 1] = True  
                   count_snakes -= 1  
               # Try to eat the right snake if it exists and is not already eaten  
               elif i < n - 1 and case[i + 1] == 's' and not eaten[i + 1]:  
                   eaten[i + 1] = True  
                   count_snakes -= 1  
       
       # Determine the results  
       if count_snakes > count_mongooses:  
           results.append("snakes")  
       elif count_mongooses > count_snakes:  
           results.append("mongooses")  
       else:  
           results.append("tie")  
   
   return results  
 
# Input processing  
T = int(input())  
test_cases = [input().strip() for _ in range(T)]  
results = determine_winner(test_cases)  
 
# Output results  
for result in results:  
   print(result)
 
4.Cutribbon
def cut_ribbon(T, cases):
   MOD = 10**9 + 7
   results = []
   
   for N, L in cases:
       # Initialize dp array
       dp = [0] * (N + 1)
       dp[0] = 1  # Base case
       
       # Loop through lengths from 1 to N
       for i in range(1, N + 1):
           for j in range(2, L + 1, 2):  # Only even lengths
               if j <= i:
                   dp[i] = (dp[i] + dp[i - j]) % MOD
       
       results.append(dp[N])
   
   return results
 
# Input handling
T = int(input())
cases = []
 
for _ in range(T):
   N, L = map(int, input().split())
   cases.append((N, L))
 
# Get results and print
results = cut_ribbon(T, cases)
for result in results:
   print(result)
