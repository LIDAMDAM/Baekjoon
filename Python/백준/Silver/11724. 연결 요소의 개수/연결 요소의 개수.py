import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
count = 0

def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for n in graph[node]:
                if not visited[n]:
                    stack.append(n)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)