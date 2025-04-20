import sys

num = ""
while(True):
    num = str(sys.stdin.readline().strip())
    ans = "yes"
    if (num == "0"):
        break
    for i in range(len(num)):
        if (num[i] != num[len(num)-i-1]):
            ans = "no"
            break
    print(ans)