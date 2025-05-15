import sys
input = sys.stdin.readline

for i in range(3):
    n = int(input().strip())
    total = 0
    for _ in range(n):
        num = int(input().strip())
        total += num
    if total > 0: print('+')
    elif total < 0: print('-')
    else: print('0')