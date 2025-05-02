import sys
input = sys.stdin.readline

num = int(input().strip())

result = 0
while(num >= 5):
    num //= 5
    result += num


print(result)