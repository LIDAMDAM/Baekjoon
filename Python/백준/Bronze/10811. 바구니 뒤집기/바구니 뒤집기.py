n, m = map(int, input().split())
lst = list()
for i in range(1, n+1):
    lst.append(i)

for j in range(m):
    a, b = map(int, input().split())
    lst[a-1:b] = lst[a-1:b][::-1]
    
print(*lst)