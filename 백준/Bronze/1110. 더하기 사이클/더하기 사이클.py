n = int(input())
if(n<10):
  t = n*11
else:
  t = (n%10+n//10)%10+n%10*10
i = 1
while(True):
  if(t == n):
    print(i)
    break
  else:
    if(t<10):
      t = t*11
    else:
      t = (t%10+t//10)%10+t%10*10
  i += 1