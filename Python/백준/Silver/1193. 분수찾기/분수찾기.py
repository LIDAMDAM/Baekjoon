x = int(input())
line, n = 1, 1

while n<x:
    line += 1
    n += line
n -= line

if line % 2 == 0:
    a = x - n
    b = line - a + 1
else:
    b = x - n
    a = line - b + 1

print(f"{a}/{b}")