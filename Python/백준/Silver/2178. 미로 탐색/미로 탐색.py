import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs():
    queue = deque([(0, 0)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            x_tmp = x+dx[i]
            y_tmp = y+dy[i]
            if x_tmp < 0 or x_tmp >= m or y_tmp < 0 or y_tmp >= n: continue
            if graph[y_tmp][x_tmp] == '0' or visited[y_tmp][x_tmp] != 0: continue
            visited[y_tmp][x_tmp] = visited[y][x]+1
            queue.append((y_tmp, x_tmp))
    return visited[n-1][m-1]

print(bfs()+1)