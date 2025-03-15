import sys

n = int(sys.stdin.readline())

for i in range(2, 2*n+1):
    space = abs(i-n-1)
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*(2*(n-space)-1))
    sys.stdout.write("\n")