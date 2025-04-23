import sys

testCase = int(input())
k, n = 0, 0

for _ in range(testCase):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    arr = [[0 for _ in range(15)] for _ in range(15)]

    for l in range(1, 15):
        arr[0][l] = l

    for i in range(1, k+1):
        for j in range(1, n+1):
            for x in range(1, j+1):
                arr[i][j] += arr[i-1][x]
    print(arr[k][n])