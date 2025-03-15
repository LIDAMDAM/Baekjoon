import sys

L = []

num = int(sys.stdin.readline())
while(num != 0):
    L.append(num%10)
    num = num//10

L.sort(reverse = True)
S = ''.join(map(str, L))
print(S)