import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        if graph[i][k] == INF: continue
        for j in range(1, n+1):
            if graph[k][j] == INF: continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

kb_num = [ sum(graph[i][1:]) for i in range(1, n+1) ]
result = kb_num.index(min(kb_num))
print(result+1)