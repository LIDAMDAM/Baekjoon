x = int(input())
n = 0
total = 1
if (x == 1):
  print(1)
else:
  while(True):
    n += 1
    total += n*6
    if (total >= x):
      print(n+1)
      break