import sys
input = sys.stdin.readline

test_case = int(input())

dp = [0]*47
dp[1] = 1
for i in range(2, 47):
    dp[i] = dp[i-1]+dp[i-2]

for _  in range(test_case):
    num =  int(input())
    array = []
    for i in range(46, 0, -1):
        if num - dp[i] >= 0:
            num -= dp[i]
            array.append(dp[i])
    array.sort()
    print(' '.join(map(str, array)))