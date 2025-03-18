import sys

n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l.sort(key = lambda x : (x[1], x[0]))

for j in range(n):
    sys.stdout.write(f'{l[j][0]} {l[j][1]}\n')