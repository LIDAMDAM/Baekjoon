import sys
input = sys.stdin.readline

test_case = int(input().strip())
result = []
for _ in range(test_case):
    wear_num = int(input().strip())
    wear_arr = {}
    for _ in range(wear_num):
        tmp, wear = input().strip().split()
        if wear in wear_arr: wear_arr[wear] += 1
        else: wear_arr[wear] = 1
    ans = 1
    for i in wear_arr.values():
        ans *= i+1
    ans -= 1
    result.append(ans)
print('\n'.join(map(str, result)))