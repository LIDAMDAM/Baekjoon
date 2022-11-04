import sys
sys.setrecursionlimit(10 ** 6)

def func(a):
    if a == 1:
        return('*')
    b = a//3
    S = func(b)
    l = []

    for i in S:
        l.append(i*3)
    for i in S:
        l.append(i+' '*b+i)
    for i in S:
        l.append(i*3)
    return l
    

num = int(sys.stdin.readline())
print('\n'.join(func(num)))