import sys
input = sys.stdin.readline

n = int(input())
square_arr = [0 if (i**0.5)%1 else 1 for i in range(n+1)]

result = 4
for i in range(int(n**0.5), 0, -1):
    if square_arr[n]:
        result = 1
        break
    elif square_arr[n-i**2]:
        result = 2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if square_arr[(n-i**2)-j**2]: result = 3

print(result)