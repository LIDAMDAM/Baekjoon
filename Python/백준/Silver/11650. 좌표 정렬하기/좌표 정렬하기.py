import sys

n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l.sort()

for j in range(n):
    sys.stdout.write(f'{l[j][0]} {l[j][1]}\n')