import sys
input = sys.stdin.readline

n = int(input().strip())
array = [list(map(int, input().strip().split())) for _ in range(n)]
n_sum = n*(n**2 + 1)//2
result = "TRUE"

for i in range(n):
    if sum(array[i]) != n_sum:
        result = "FALSE"
        break

if result == "TRUE":
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += array[j][i]
        if tmp != n_sum:
            result = "FALSE"
            break

if result == "TRUE":
    tmp = 0
    for i in range(n):
        tmp += array[i][i]
    if tmp != n_sum:
        result = "FALSE"
    tmp = 0
    for i in range(n-1, -1, -1):
        tmp += array[i][i]
    if tmp != n_sum:
        result = "FALSE"

if result == "TRUE":
    for i in range(n):
        if len(set(array[i])) != n:
            result = "FALSE"

print(result)