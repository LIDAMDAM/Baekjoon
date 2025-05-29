import sys

num = int(input())
a = []
a.extend(list(map(int, sys.stdin.readline().split())))
ans = int(0)
if 1 in a:
  a.remove(1)
test = int(0)

for i in a:
    for j in range(2, i):
        if(i%j == 0):
            test += 1
    if (test == 0):
        ans += 1
    test = 0
print(ans)