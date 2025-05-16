import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for n in sorted(graph[node], reverse=True):
                if not visited[n]:
                    stack.append(n)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for n in sorted(graph[node]):
            if not visited[n]:
                visited[n] = True
                queue.append(n)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)