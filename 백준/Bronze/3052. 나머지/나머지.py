import sys

a = set()
for i in range(10):
  a.add((int(sys.stdin.readline()))%42)
i = 0
while(True):
  try:
    a.pop()
    i += 1
  except:
    print(i)
    break