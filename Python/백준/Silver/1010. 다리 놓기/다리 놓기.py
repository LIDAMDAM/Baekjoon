import sys

input = sys.stdin.readline

def fac(a):
    n = 1
    for i in range(2, a+1):
        n *= i
    return n

def comb(a, b):
    return(fac(a)//(fac(a-b)*fac(b)))

testCase = int(input().strip())
for _ in range(testCase):
    n, m = map(int, input().split())
    print(comb(m, n))