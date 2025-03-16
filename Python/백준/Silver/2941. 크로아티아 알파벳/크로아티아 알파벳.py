import sys

ca = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = str(sys.stdin.readline().strip())

for i in ca:
    s = s.replace(i,'!')
print(len(s))