import sys
input = sys.stdin.readline

while (True):
    length = list(map(int, input().strip().split()))
    if (length[0] == 0): break
    length.sort()
    print("right" if length[0]**2 + length[1]**2 == length[2]**2 else "wrong")