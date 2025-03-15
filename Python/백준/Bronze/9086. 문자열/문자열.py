import sys

n = int(input())

for i in range(n):
    s = str(sys.stdin.readline().strip())
    print(s[0] + s[-1])