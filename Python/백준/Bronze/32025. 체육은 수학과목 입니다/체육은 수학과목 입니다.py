import sys
input = sys.stdin.readline

h = int(input())
w = int(input())
print(h*50 if h < w else w*50)