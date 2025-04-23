import sys

n = int(input())
setN = set(map(int, sys.stdin.readline().split()))
m = int(input())
listM = list(map(int, sys.stdin.readline().split()))
ansNum = set(set(listM) & setN)
ansArray = list()

for i in listM:
    if i in ansNum:
        ansArray.append(1)
    else: ansArray.append(0)

print(' '.join(map(str, ansArray)))