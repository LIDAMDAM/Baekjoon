import sys
from collections import Counter

input = sys.stdin.readline

result = []

N = int(input().strip())
nArray = Counter(map(int, input().split()))
M = int(input().strip())
mArray = list(map(int, input().split()))

for i in mArray:
    result.append(nArray[i])

print(" ".join(map(str, result)))