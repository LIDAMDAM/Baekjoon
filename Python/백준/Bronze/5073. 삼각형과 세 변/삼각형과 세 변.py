import sys

a, b, c = 0, 0, 0

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    if a >= b + c:
        print("Invalid")
    elif b >= a + c:
        print("Invalid")
    elif c >= a + b:
        print("Invalid")
    else:
        if a == b and b == c:
            print("Equilateral")
        elif a == b:
            print("Isosceles")
        elif a == c:
            print("Isosceles")
        elif b == c:
            print("Isosceles")
        else:
            print("Scalene")