import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1] *100001

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        node = queue.popleft()
        if node == k:
            print(visited[node])
            break
        for next_node in (node - 1, node + 1, node * 2):
            if 0 <= next_node < 100001 and visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

bfs(n)