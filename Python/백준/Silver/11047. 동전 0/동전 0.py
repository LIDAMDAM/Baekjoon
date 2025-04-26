import sys

input = sys.stdin.readline

count = 0
n, k = map(int, input().split())
moneyArray = [int(input().strip()) for _ in range(n)]

for i in reversed(moneyArray):
    count += k//i
    k %= i

print(count)