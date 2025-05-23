import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = 1, max(array)
total = 0
while start <= end:
    mid = (start+end)//2
    total = sum(i-mid for i in array if i >= mid)
    if total >= m: start = mid+1
    else: end = mid-1

print(end)