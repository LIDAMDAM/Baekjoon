import sys

arr = []
x, y = 0, 0
maxi = 0
for _ in range(9):
    arr.extend([list(map(int, sys.stdin.readline().split()))])
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxi:
            maxi = arr[i][j]
            x = i
            y = j
print(maxi)
print(x+1, y+1)