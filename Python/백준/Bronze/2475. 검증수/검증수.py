import sys

lst = map(int, sys.stdin.readline().split())
total = int(0)

for i in lst:
    i = i**2
    total += i

print(total%10)