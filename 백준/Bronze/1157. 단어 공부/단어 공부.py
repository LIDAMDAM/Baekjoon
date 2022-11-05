import sys
all = str(sys.stdin.readline().rstrip())
all = all.upper()

alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
maxinum = int(0)
maxialpa = '?'


for i in alpa:
    t = all.count(i)
    if t > maxinum:
        maxialpa = i
        maxinum = t
    elif t == maxinum:
        maxialpa = '?'

print(maxialpa)