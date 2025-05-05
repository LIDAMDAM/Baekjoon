import sys
input = sys.stdin.readline

test_case = int(input().rstrip())
num_list = list(map(int, input().rstrip().split()))
num_sort = sorted(list(set(num_list)))

num_dict = {num: idx for idx, num in enumerate(num_sort)}
result = [num_dict[i] for i in num_list]

print(' '.join(map(str, result)))