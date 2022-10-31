n = int(input())
a = list(map(int, input().split()))
v = int(input())
j = int(0)
for i in a:
  if v == i:
    j += 1
print(j)