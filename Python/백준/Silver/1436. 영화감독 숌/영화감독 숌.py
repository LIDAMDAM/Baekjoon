n = int(input())
count = 0
c = 0

while True:
    c += 1
    if "666" in str(c):
        count += 1
        if count == n:
            break

print(c)