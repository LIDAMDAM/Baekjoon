import sys

N = int(input())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))
  
num.sort()

for _ in num:
    print(_)