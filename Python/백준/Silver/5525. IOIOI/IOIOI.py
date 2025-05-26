import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0
i = 0
while i<m-1:
    if s[i] == "I" and s[i+1] == 'O':
        length = 0
        while i+2<m and s[i+1] == 'O' and s[i+2] == 'I':
            length += 1
            i += 2
        if length >= n: count += (length-n+1)
    i += 1

print(count)