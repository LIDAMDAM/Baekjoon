import sys
input = sys.stdin.readline

test_case = int(input().strip())
for _ in range(test_case):
    h, w, n = map(int, input().strip().split())
    
    floor = n % h
    room = n // h +1
    if (floor == 0):
        floor = h
        room -= 1
    print(floor * 100 + room)