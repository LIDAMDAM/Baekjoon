import sys
input = sys.stdin.readline

test_case = int(input().strip())
num_array = [int(input().strip()) for _ in range(test_case)]
num_array.sort()

num_count = [0]*8001
for i in num_array:
    num_count[i+4000] += 1
max_num = max(num_count)
mode = [index-4000 for index, value in enumerate(num_count) if value == max_num]
mode.sort()

print(round(sum(num_array)/test_case))
print(num_array[test_case//2])
print(mode[1] if len(mode) > 1 else mode[0])
print(num_array[-1] - num_array[0])