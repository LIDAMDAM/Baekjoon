import sys

c = int(input())
for i in range(c):
  s = list(map(int, sys.stdin.readline().split()))
  s.reverse()
  x = s.pop()
  z = 0
  ans = sum(s)/x
  for j in range(x):
    if(s.pop() > ans):
      z += 1
  print('%.3f%%' %(z/x*100))