import sys
input = sys.stdin.readline

num = int(input())
score = [0] + [int(input()) for _ in range(num)]

dp = [0]*(num+1)
dp[1] = score[1]
if num>1: dp[2] = score[1]+score[2]
for i in range(3, num+1):
    dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

print(dp[num])