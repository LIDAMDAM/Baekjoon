import sys
input = sys.stdin.readline

num = int(input().strip())
dp = [0]*1001
dp[1] = 1
dp[2] = 2

if num > 2:
    for i in range(3, num+1):
        dp[i] = (dp[i-1]+dp[i-2])%10007
print(dp[num])