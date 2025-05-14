import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = graph[b][a] = 1

visit = [0]*(n+1)
result = []

def bfs(v):
    queue = [v]
    visit[v] = 1
    while queue:
        v = queue.pop(0)
        result.append(v)
        for i in range(1, n+1):
            if visit[i] == 0 and graph[i][v] == 1:
                queue.append(i)
                visit[i] = 1

bfs(1)
print(len(result)-1)