[9/25, 8:34 AM] Abdul (KLU): import os

def child_process():
    print(f"Child process ID: {os.getpid()}")

def main():
    pid = os.fork()
    if pid == 0:
        child_process()
    else:
        print(f"Parent process ID: {os.getpid()}, Child process ID: {pid}")

if __name__ == "__main__":
    main()
[9/25, 8:34 AM] Abdul (KLU): def bankers_algorithm(processes, max_resources, allocated_resources, need_resources):
    available_resources = [max_resources[i] - sum(allocated_resources[j][i] for j in range(len(processes))) for i in range(len(max_resources))]
    finish = [False] * len(processes)
    safe_sequence = []

    while len(safe_sequence) < len(processes):
        for i in range(len(processes)):
            if not finish[i] and all(need_resources[i][j] <= available_resources[j] for j in range(len(available_resources))):
                safe_sequence.append(processes[i])
                finish[i] = True
                available_resources = [available_resources[j] + allocated_resources[i][j] for j in range(len(available_resources))]
                break
        else:
            print("No safe sequence found. System is in a deadlock.")
            return

    print("Safe sequence:", safe_sequence)

processes = ["P1", "P2", "P3"]
max_resources = [10, 5, 7]
allocated_resources = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
need_resources = [[7, 5, 3], [2, 0, 0], [0, 0, 0]]
bankers_algorithm(processes, max_resources, allocated_resources, need_resources)
[9/25, 8:34 AM] Abdul (KLU): def sjf_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by burst time
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

processes = [("P1", 6), ("P2", 8), ("P3", 7)]
sjf_scheduling(processes)
[9/25, 8:34 AM] Abdul (KLU): def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    print("Process\tBlock")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i}\t{allocation[i]}")
        else:
            print(f"{i}\tNot Allocated")

blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
first_fit(blocks, processes)
[9/25, 8:34 AM] Abdul (KLU): def fcfs_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

processes = [("P1", 5), ("P2", 3), ("P3", 8)]
fcfs_scheduling(processes)
