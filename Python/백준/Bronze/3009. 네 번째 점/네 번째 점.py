import sys

l = []
ans = []
for i in range(3):
    l.append(list(sys.stdin.readline().split()))

for j in range(2):
    if l[0][j] == l[1][j]: ans.append(l[2][j])
    elif l[0][j] == l[2][j]: ans.append(l[1][j])
    else: ans.append(l[0][j])

print(*ans)