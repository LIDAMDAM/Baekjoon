import sys

testCase = int(input())
center = 0
numList = list(map(int, sys.stdin.readline().split()))

print(min(numList)*max(numList))