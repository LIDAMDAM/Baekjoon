import sys
input = sys.stdin.readline

test_case = int(input())
grade_arr = [input().split() for _ in range(test_case)]
grade_arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

sys.stdout.write('\n'.join(grade_arr[i][0] for i in range(test_case)))