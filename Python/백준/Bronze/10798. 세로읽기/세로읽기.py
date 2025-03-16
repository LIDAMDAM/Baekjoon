import sys

a = [[],[],[],[],[]]
l = []

for i in range(5):
    a[i] = list(sys.stdin.readline().strip())
    l.append(len(a[i]))
max_l = max(l)

for j in range(max_l):
    for k in range(5):
       if l[k] > j:
           sys.stdout.write(str(a[k][j]))