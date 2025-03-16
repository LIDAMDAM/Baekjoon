n, b = input().split()
b = int(b)
total = 0
l = len(n) - 1

for i in n:
    if i.isalpha():
        i = ord(i) - 55
    else:
        i = int(i)
    total += i * (b ** l)
    l -= 1

print(total)