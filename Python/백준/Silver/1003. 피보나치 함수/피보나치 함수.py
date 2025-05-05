import sys
input = sys.stdin.readline

fibo = [[0, 0] for _ in range(41)]
fibo[0], fibo[1] = [1, 0], [0, 1]
for i in range(2, 41):
    fibo[i][0] = fibo[i-1][0]+fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1]+fibo[i-2][1]

test_case = int(input().rstrip())
for _ in range(test_case):
    num = int(input().rstrip())
    print(fibo[num][0], fibo[num][1])