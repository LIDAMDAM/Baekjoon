y, x = map(int, input().split())
a, b =[],[]
for i in range(y):
  i = list(map(int, input().split()))
  a.append(i)
for i in range(y):
  i = list(map(int, input().split()))
  b.append(i)
for i in range(y):
  for j in range(x):
    print(a[i][j] + b[i][j], end = ' ')
  print()