import sys

while(True):
  try:
    a, b = map(int, sys.stdin.readline().split())
  except:
    break
  else:
    print(a+b)