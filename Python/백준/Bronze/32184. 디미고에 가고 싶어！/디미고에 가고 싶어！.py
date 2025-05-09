import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())
result = (b-a)//2
print(result+2 if a%2 == 0 and b%2 == 1 else result+1)