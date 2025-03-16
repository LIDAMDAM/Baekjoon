import sys

t = int(input())

for i in range(t):
    c = int(sys.stdin.readline().strip())
    q ,c = c//25, c%25
    d, c = c//10, c%10
    n, c = c//5, c%5
    p = c//1
    print(q, d, n, p)