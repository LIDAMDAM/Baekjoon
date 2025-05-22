import sys
input = sys.stdin.readline

string = input().strip()
sum_arr = list(map(str, string.split('-')))
for i in range(len(sum_arr)):
	sum_arr[i] = sum(map(int, sum_arr[i].split('+')))

result = sum_arr[0]
for i in range(1, len(sum_arr)):
		result -= sum_arr[i]

print(result)