import sys
input = sys.stdin.readline

string = input().strip()
count = 1
tmp = 0
for i in string:
    if ord(i) <= tmp:
        count += 1
    tmp = ord(i)
print(count)