import sys

input = sys.stdin.readline
print = sys.stdout.write

result = []

_ = input()
orignalNum = set(map(int, input().split()))

_ = input()
findNum = list(map(int, input().split()))

for i in findNum:
    if i in orignalNum: result.append('1')
    else: result.append('0')

print('\n'.join(result) + '\n')