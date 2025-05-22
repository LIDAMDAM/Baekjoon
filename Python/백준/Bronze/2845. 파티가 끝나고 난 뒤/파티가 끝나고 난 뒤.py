import sys
input = sys.stdin.readline

l, p = map(int, input().split())
array = list(map(int, input().split()))
for i in range(5):
    array[i] = array[i]-l*p
print(' '.join(map(str, array)))