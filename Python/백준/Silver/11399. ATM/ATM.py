import sys
input = sys.stdin.readline

test_case = int(input().strip())
time_list = list(map(int, input().strip().split()))
time_list.sort()

result = 0
for i in range(test_case):
    result += time_list[i]*(test_case-i)

print(result)