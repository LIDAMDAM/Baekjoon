import sys

input = sys.stdin.readline

testCase = int(input())
name, inout = "", ""
inoutList = set()
for _ in range(testCase):
    name, inout = map(str, input().split())
    if (inout == "enter"):
        inoutList.add(name)
    else: inoutList.remove(name)

inoutList = list(inoutList)
inoutList.sort(reverse = True)

for i in inoutList:
    print(i)