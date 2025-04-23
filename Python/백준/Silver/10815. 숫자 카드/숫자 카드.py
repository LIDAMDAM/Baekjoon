import sys

input = sys.stdin.readline

n = int(input())
setN = set(map(int, input().split()))
m = int(input())
listM = list(map(int, input().split()))

ansArray = []

for i in listM:
    if i in setN:
        ansArray.append("1")
    else: ansArray.append("0")

print(' '.join(ansArray))