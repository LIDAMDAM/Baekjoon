import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n >= m:
    print(0)
else:
	result = 1
	for i in range(2, n+1): result = (result*i)%m
	print(result)