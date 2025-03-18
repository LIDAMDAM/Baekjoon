n = int(input())
l = []
for i in range(1667):
  for j in range(1001):
    if 3*i+5*j == n:
      l.append(i+j)
if len(l) == 0:
  l.append(-1)
l.sort()
print(l[0])