import sys
from collections import deque
input = sys.stdin.readline

add_x = [-1, 1, 0, 0]
add_y = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x = x+add_x[i]
            temp_y = y+add_y[i]
            if n > temp_x >= 0 and m > temp_y >=0:
                if ground[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                    queue.append((temp_x, temp_y))
                    visited[temp_x][temp_y] = True


test_case = int(input())
for _ in range(test_case):
    m, n, k = map(int, input().split())
    ground = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(k):
        a, b = map(int, input().split())
        ground[b][a] = 1
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)