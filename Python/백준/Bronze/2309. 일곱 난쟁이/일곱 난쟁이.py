import sys

num = []
for i in range(9):
    num.append(int(sys.stdin.readline().strip()))
find, total = 0, 0
total = sum(num)

for i in range(9):
    for j in range(9):
        if(i != j):
            if(total - num[i] - num[j] == 100):
                num.remove(num[i])
                num.remove(num[j-1])
                find = 1
                break
    if (find == 1): break

num.sort()
for i in range(7):
    print(num[i])