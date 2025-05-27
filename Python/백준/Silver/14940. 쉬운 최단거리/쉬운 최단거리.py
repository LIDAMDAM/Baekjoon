import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=m or \
            visited[ny][nx] != 0 or graph[ny][nx] == 0: continue
            visited[ny][nx] = visited[y][x]+1
            queue.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] == 1: visited[i][j] = -1
    visited[start_y][start_x] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            for i in range(n): print(*visited[i])
            exit