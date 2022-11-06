import sys

num = []
r = int(input())

for i in range(r):
    num.append(int(sys.stdin.readline()))
num.sort()

for j in num:
    print(j)