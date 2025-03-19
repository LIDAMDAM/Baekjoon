import sys

n = int(input())
l = []
a = ''


for i in range(n):
    a = str(sys.stdin.readline().strip())
    if a not in l:
        l.append(a)

l.sort(key = lambda x : (len(x), x))

for i in l:
    sys.stdout.write(f"{i}\n")