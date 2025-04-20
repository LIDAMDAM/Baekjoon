import sys

a, b = map(str, sys.stdin.readline().split())
sumA, sumB = 0, 0
for i in a:
    sumA += int(i)
for j in b:
    sumB += int(j)

print(sumA*sumB)