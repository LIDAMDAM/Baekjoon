import sys

N, k = map(int, input().split())
x = list(map(int, sys.stdin.readline().split()))
x.sort(reverse=True)
print(x[k-1])