import sys

lst = []

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    lst = []
    temp = 0
    for i in range(1, n):
        if n%i == 0:
            lst.append(i)
    for j in range(len(lst)):
        temp += int(lst[j])
    if temp == n:
        sys.stdout.write(f'{n} = {lst[0]}')
        for k in range(1, len(lst)):
            sys.stdout.write(f' + {lst[k]}')
        sys.stdout.write('\n')
    else:
        sys.stdout.write(f'{n} is NOT perfect.\n')