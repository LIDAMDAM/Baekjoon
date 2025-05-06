import sys
input = sys.stdin.readline

num = int(input())
dp = [0]*(num+1)
for i in range(2, num+1):
    best = dp[i-1]
    if i%3 == 0:
        if dp[i//3] < best: best = dp[i//3]
    if i%2 == 0:
        if dp[i//2] < best: best = dp[i//2]
    dp[i] = best+1

print(dp[num])