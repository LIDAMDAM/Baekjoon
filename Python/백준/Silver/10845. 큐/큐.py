import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
test_case = int(input().strip())
result = []
for _ in range(test_case):
    command = input().strip().split()
    if (command[0] == "push"):
        queue.append(int(command[1]))
    elif (command[0] == "pop"):
        result.append(queue.popleft() if queue else -1)
    elif (command[0] == "size"):
        result.append(len(queue))
    elif (command[0] == "empty"):
        result.append(0 if queue else 1)
    elif (command[0] == "front"):
        result.append(queue[0] if queue else -1)
    elif (command[0] == "back"):
        result.append(queue[len(queue)-1] if queue else -1)

print("\n".join(map(str, result)))