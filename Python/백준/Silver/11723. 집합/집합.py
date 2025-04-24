import sys

input = sys.stdin.readline

testCase = int(input().strip())
S = set()

for _ in range(testCase):
    tmp = input().strip().split()

    if(tmp[0] == "add"):
        S.add(int(tmp[1]))
    elif(tmp[0] == "remove"):
        S.discard(int(tmp[1]))
    elif(tmp[0] == "check"):
        if int(tmp[1]) in S: print(1)
        else: print(0)
    elif(tmp[0] == "toggle"):
        if int(tmp[1]) in S: S.remove(int(tmp[1]))
        else: S.add(int(tmp[1]))
    elif(tmp[0] == "all"):
        S = set(range(1, 21))
    elif(tmp[0] == "empty"):
        S.clear()