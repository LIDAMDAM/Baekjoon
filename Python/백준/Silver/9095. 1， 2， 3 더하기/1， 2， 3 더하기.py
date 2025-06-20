import sys
input = sys.stdin.readline

test_case = int(input())

dp = [0]*12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for _ in range(test_case):
    num = int(input())
    print(dp[num])