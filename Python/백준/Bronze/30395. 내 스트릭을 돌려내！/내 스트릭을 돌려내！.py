import sys
input = sys.stdin.readline

day = int(input().strip())
problem_array = list(map(int, input().strip().split()))
solve_day = 0
streak = []

for i in range(day):
    if problem_array[i] == 0:
        if i+1 != day:
            if problem_array[i+1] == 0:
                streak.append(solve_day)
                solve_day = 0
    else: solve_day += 1
streak.append(solve_day)

print(max(streak))