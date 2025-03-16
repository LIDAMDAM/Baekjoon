import sys
n = int(input())

while n % 2 == 0:
    sys.stdout.write("2\n")
    n //= 2

i = 3
while i * i <= n:
    while n % i == 0:
        sys.stdout.write(f"{i}\n")
        n //= i
    i += 2

if n > 1:
    sys.stdout.write(f"{n}\n")
