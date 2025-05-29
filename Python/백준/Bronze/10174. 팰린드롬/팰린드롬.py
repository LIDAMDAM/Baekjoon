import sys
input = sys.stdin.readline

test_case = int(input())
for i in range(test_case):
    string = input().rstrip('\n')
    print("Yes" if string.lower() == string.lower()[::-1] else "No")