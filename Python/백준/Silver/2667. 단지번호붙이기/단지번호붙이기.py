import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*n  for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []
count = 0

def dfs(y, x):
    stack = ([(y, x)])
    visited[y][x] = True
    size = 0
    while stack:
        y, x = stack.pop()
        size += 1
        for k in range(4):
            y_tmp, x_tmp = y+dy[k], x+dx[k]
            if x_tmp < 0 or x_tmp >= n or y_tmp < 0 or y_tmp >= n: continue
            if not visited[y_tmp][x_tmp] and graph[y_tmp][x_tmp] == '1':
                stack.append((y_tmp, x_tmp))
                visited[y_tmp][x_tmp] = True
    return size

for i in range(n):
    for j in range(n):
        if visited[i][j] or graph[i][j] =='0': continue
        result.append(dfs(i, j))
        count += 1

print(count)
print('\n'.join(map(str, sorted(result))))