import sys
input = sys.stdin.readline

a, i = map(int, input().strip().split())
print((i-1)*a+1)