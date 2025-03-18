n = int(input())
ansl = []
ans = 0

for i in range(n, 0, -1):
    ans = i + sum(map(int, str(i)))
    if n == ans:
        ansl.append(i)

if not ansl:
    print(0)
else:
    print(min(ansl))