import sys

num = []

for _ in range(5):
    num.append(int(sys.stdin.readline()))

num.sort()
ans = int(sum(num)/5)
print(ans)
print(num[2])