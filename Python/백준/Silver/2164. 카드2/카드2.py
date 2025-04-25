import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
qNum = deque(range(1, N+1))

while(len(qNum) > 1):
    qNum.popleft()
    qNum.append(qNum.popleft())

print(qNum.pop())