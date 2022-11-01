p = [[0]*100 for _ in range(100)]
count = int(0)
num = int(input())
for i in range(num):
    y, x = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            if p[j][k] == 0:
                p[j][k] = 1
                count += 1
print(count)