import sys
input = sys.stdin.readline

n, k, t0 = map(int, input().strip().split())
d_array = list(map(int, input().strip().split()))
t = t0
result = 0
for i in range(n):
    if t>k: t = t+d_array[i] - abs(t-k)
    elif t<k: t = t+d_array[i] + abs(t-k)
    else: t += d_array[i]
    result += abs(t-k)

print(result)