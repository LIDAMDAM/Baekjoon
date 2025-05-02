import sys
input = sys.stdin.readline

while(True):
    stack = []
    result = "yes"
    string = input().rstrip()
    if string == ".": break
    for i in range(len(string)):
        if string[i] == '(': stack.append('(')
        elif string[i] == '[': stack.append('[')
        elif string[i] == ')':
            if stack:
                if stack.pop() == '[':
                    result = "no"
                    break
            else: 
                result = "no"
                break
        elif string[i] == ']':
            if stack: 
                if stack.pop() == '(':
                    result = "no"
                    break
            else: 
                result = "no"
                break

    if stack: result = "no"
    print(result)