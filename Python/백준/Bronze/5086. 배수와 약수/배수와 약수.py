import sys

n, m = 1, 1

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    if m%n == 0:
        sys.stdout.write("factor\n")
    elif n%m == 0:
        sys.stdout.write("multiple\n")
    else:
        sys.stdout.write("neither\n")