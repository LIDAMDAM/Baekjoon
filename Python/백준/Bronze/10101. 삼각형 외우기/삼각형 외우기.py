import sys

l = []
for i in range(3):
    l.append(int(sys.stdin.readline().strip()))
if(l[0] + l[1] + l[2]) == 180:
    if(l[0] == l[1] and l[1] == l[2]):
        print("Equilateral")
    else:
        if(l[0] == l[1]):
            print("Isosceles")
        elif(l[0] == l[2]):
            print("Isosceles")
        elif(l[1] == l[2]):
            print("Isosceles")
        else:
            print("Scalene")
else:
    print("Error")