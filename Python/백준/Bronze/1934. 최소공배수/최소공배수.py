import sys

testCase = int(input())
for _ in range(testCase):
    a, b  = map(int, sys.stdin.readline().split())
    tmp1, tmp2 = a, b
    if (a < b): a, b = b, a
    while(b != 0):
        a, b = b, a%b
    print(int(tmp1*tmp2/a))