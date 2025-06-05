import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().split()))
counter = Counter(arr)
max_counter = max(counter.values())
print(min(k for k, v in counter.items() if v == max_counter))