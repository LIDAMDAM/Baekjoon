import sys
input = sys.stdin.readline

x, y = map(int, input().split())
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
num = 0
if x == 1: print(day_of_the_week[(num + y)%7])
else:
    for i in range(x-1):
        num += arr[i]
    print(day_of_the_week[(num + y)%7])