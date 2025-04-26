import sys
from collections import deque

input = sys.stdin.readline

length, remove_num = map(int, input().split())
num_array = deque(range(1, length+1))

result = []
for _ in range(length):
    num_array.rotate(-(remove_num - 1))
    result.append(num_array.popleft())

print("<" + ", ".join(map(str, result)) + ">")