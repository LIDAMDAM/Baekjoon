import sys
input = sys.stdin.readline

string = input().strip()
total = 0
for i in range(len(string)-1):
    if string[i] == '*':
        tmp = i
    else:
        if i%2 == 0: total += int(string[i])
        else: total += int(string[i])*3

if tmp%2 == 0: tmp = 1
else: tmp = 3
for i in range(10):
    if (total + i*tmp + int(string[-1]))%10 == 0:
        print(i)
        break