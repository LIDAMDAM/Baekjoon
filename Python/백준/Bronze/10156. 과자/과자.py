import sys
input = sys.stdin.readline

price, number, money = map(int, input().rstrip().split())
print(price*number-money if price*number > money else 0)