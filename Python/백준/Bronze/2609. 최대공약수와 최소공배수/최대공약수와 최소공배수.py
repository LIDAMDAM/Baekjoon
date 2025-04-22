import sys

a, b = map(int, sys.stdin.readline().split())
tmp1, tmp2 = a, b

while(True):
    if (tmp1 < tmp2):
            tmp1, tmp2 = tmp2, tmp1
    tmp1, tmp2 = tmp2, tmp1 % tmp2
    if (tmp2 == 0):
          break

print(tmp1)
print(int(a*b/tmp1))