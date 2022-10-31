total = int(input())
n = int(input())
tt = int(0)
while n != 0:
  n -= 1
  a,b = map(int, input().split())
  tt += a*b
if tt == total:
  print('Yes')
else:
  print('No')