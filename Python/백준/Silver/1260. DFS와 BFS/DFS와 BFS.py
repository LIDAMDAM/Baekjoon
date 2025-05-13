import sys
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = graph[b][a] = 1

visit_dfs = [0]*(n+1)
visit_bfs = [0]*(n+1)
result_dfs = []
result_bfs = []

def dfs(v):
    visit_dfs[v] = 1
    result_dfs.append(v)
    for i in range(1, n+1):
        if graph[v][i] == 1 and visit_dfs[i] == 0:
            dfs(i)

def bfs(v):
    queue = [v]
    visit_bfs[v] = 1
    while queue:
        v = queue.pop(0)
        result_bfs.append(v)
        for i in range(1, n+1):
            if graph[v][i] == 1 and visit_bfs[i] == 0:
                queue.append(i)
                visit_bfs[i] = 1

dfs(v)
print(' '.join(map(str, result_dfs)))
bfs(v)
print(' '.join(map(str, result_bfs)))