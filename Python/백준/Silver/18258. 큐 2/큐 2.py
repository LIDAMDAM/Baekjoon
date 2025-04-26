import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
test_case = int(input().strip())
for _ in range(test_case):
    command = input().strip().split()
    if (command[0] == "push"): queue.append(command[1])
    elif (command[0] == "pop"): print(queue.popleft() if queue else -1)
    elif (command[0] == "size"): print(len(queue))
    elif (command[0] == "empty"): print(0 if queue else 1)
    elif (command[0] == "front"): print(queue[0] if queue else -1)
    elif (command[0] == "back"): print(queue[-1] if queue else -1)