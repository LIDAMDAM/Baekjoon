import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for i in range(n)]
array.sort()
for i in array: print(i)