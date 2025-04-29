import sys
input = sys.stdin.readline

lst = []
str_set = set(["FizzBuzz", "Fizz", "Buzz"])
for i in range(3):
    lst.append(str(input().strip()))
    if (lst[i] in str_set):
        continue
    else:
        result = int(lst[i])+3-i
        break
if (result%3 == 0 and result%5 == 0): result = "FizzBuzz"
elif (result%3 == 0): result = "Fizz"
elif (result%5 == 0): result = "Buzz"

print(result)