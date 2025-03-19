import sys

n = int(input())
l = []

for i in range(n):
    l.append(list(map(str, sys.stdin.readline().split())))

l.sort(key = lambda x : int(x[0]))

for i in range(n):
    sys.stdout.write(f"{l[i][0]} {l[i][1]}\n")