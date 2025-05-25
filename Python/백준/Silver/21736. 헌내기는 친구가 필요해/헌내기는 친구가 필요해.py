import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

y, x = map(int, input().split())
arr = [list(input().strip()) for _ in range(y)]
visited = [[False]*x for _ in range(y)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def dfs(y_tmp, x_tmp):
    global result
    if x_tmp < 0 or x_tmp >= x or y_tmp < 0 or y_tmp >= y: return
    if visited[y_tmp][x_tmp] == True or arr[y_tmp][x_tmp] == 'X': return
    visited[y_tmp][x_tmp] = True
    if arr[y_tmp][x_tmp] =='P': result += 1
    for i in range(4):
        dfs(y_tmp+dy[i], x_tmp+dx[i])

flag = False
for i in range(y):
    for j in range(x):
        if arr[i][j] == 'I':
            dfs(i, j)
            flag = True
            break
    if flag: break
print("TT" if result == 0 else result)