import sys
from collections import deque

input = sys.stdin.readline

testCase = int(input().strip())
for _ in range(testCase):
    stack = []
    result = True
    string = (input().strip())
    for i in string:
        if (i == '('):
            stack.append(i)
        elif (i == ')'):
            if stack:
                stack.pop()
            else:
                result = False
                break

    if stack:
        result = False
    print("YES" if result else "NO")