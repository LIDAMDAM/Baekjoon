import sys
input = sys.stdin.readline

chicken_number = int(input().rstrip())
coke, beer = map(int, input().rstrip().split())
drink = coke//2 + beer
print(drink if drink < chicken_number else chicken_number)