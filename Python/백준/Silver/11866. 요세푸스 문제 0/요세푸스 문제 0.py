import sys
from collections import deque
input = sys.stdin.readline

result = []
person_num, remove_num = map(int, input().strip().split())
queue = deque(range(1, person_num+1))
for _ in range(person_num):
    queue.rotate(-(remove_num))
    result.append(queue.pop())

print("<" + ", ".join(map(str, result)) + ">")