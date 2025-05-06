import sys
input = sys.stdin.readline

num, test_case = map(int, input().split())
num_array = list(map(int, input().split()))

dp = [0]*(num+1)
for i in range(1, num+1):
    dp[i] = dp[i-1]+num_array[i-1]

result = []
for _ in range(test_case):
    a, b = map(int, input().split())
    result.append(dp[b] - dp[a-1])
print('\n'.join(list(map(str, result))))