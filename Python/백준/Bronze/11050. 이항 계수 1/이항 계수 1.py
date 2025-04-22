import sys

def fac(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

n, k = map(int ,sys.stdin.readline().split())
print(int(fac(n)/(fac(n-k)*fac(k))))