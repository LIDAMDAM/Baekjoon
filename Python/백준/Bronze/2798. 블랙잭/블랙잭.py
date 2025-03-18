n, m = map(int, input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)
e = []

for i in range(n):
    if l[i] >= m:
        continue
    else:
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i]+l[j]+l[k] <= m:
                    e.append(l[i]+l[j]+l[k])
print(max(e))