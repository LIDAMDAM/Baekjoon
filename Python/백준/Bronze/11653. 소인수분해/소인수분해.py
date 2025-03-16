import sys
n = int(input())

for i in range(2, n+1):
    if n == 0:
        break
    elif n%i == 0:
        while n%i == 0:
            n /= i
            sys.stdout.write(f"{str(i)}\n")