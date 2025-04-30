import sys
input = sys.stdin.readline

def user_round(a):
    return int(a+0.5)

test_case = int(input().strip())

if (test_case == 0):
    print(0)
    sys.exit()

level_array = []
for _ in range(test_case):
    level_array.append(int(input().strip()))

level_array.sort()
over_level = user_round(test_case*0.15)

level_array = level_array[over_level:test_case-over_level]
print(user_round(sum(level_array)/len(level_array)))