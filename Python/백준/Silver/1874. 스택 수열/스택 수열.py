import sys
input = sys.stdin.readline

num = int(input().strip())
num_list = [i for i in range(num, 0, -1)]
result = [int(input().strip()) for _ in range(num)]
stack = []
result.reverse()
end = []

while(True):
    if stack:
        if stack[-1] == result[-1]:
            stack.pop()
            result.pop()
            end.append('-')
        else:
            if num_list:
                stack.append(num_list.pop())
                end.append('+')
            else:
                end = []
                break
    else:
        if num_list:
            stack.append(num_list.pop())
            end.append('+')
        else: break

print('\n'.join(end) if end else "NO")