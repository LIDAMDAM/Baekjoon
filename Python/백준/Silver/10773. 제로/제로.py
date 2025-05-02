import sys
input = sys.stdin.readline

test_case = int(input().strip())
stack = []
for _ in range(test_case):
    tmp = int(input().strip())
    if tmp == 0: stack.pop()
    else: stack.append(tmp)

print(sum(stack))