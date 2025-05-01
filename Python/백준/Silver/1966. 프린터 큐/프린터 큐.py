import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input().strip())

for _ in range(test_case):
    result = []
    document_count, document_order = map(int, input().strip().split())
    document_queue = deque(map(int, input().strip().split()))
    index_queue = deque(range(document_count))
    while (document_queue):
        if (document_queue[0] < max(document_queue)):
            document_queue.rotate(-1)
            index_queue.rotate(-1)
        else:
            document_queue.popleft()
            index = index_queue.popleft()
            result.append(index)
            if (index == document_order): print(len(result))