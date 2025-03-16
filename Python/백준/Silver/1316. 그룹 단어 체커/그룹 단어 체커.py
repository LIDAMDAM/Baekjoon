import sys

n = int(input())
count = int(0)
lst = list()
total = n

for i in range(n):
    s = sys.stdin.readline().strip()
    lst.clear()
    num = int(0)

    for j in s:
        if len(lst) == 0:
            lst.append(j)
        elif lst[num] != j:
            if (lst.count(j) == 0):
                num += 1
                lst.append(j)
            else:
                total -= 1
                break
print(total)