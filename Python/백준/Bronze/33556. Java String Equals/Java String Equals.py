import sys
input = sys.stdin.readline

def equals(A, B):
    if A == "null": return "NullPointerException"
    if B == "null": return "false"
    else: return "true" if A == B else "false"

def equalsIsIgnoreCase(A, B):
    if A == "null": return "NullPointerException"
    if B == "null": return "false"
    return "true" if A.upper() == B.upper() else "false"

A = input().rstrip()
B = input().rstrip()

print(equals(A, B))
print(equalsIsIgnoreCase(A, B))