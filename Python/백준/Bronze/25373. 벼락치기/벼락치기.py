import sys
input = sys.stdin.readline

def my_sum(num):
    tmp = 0
    for i in range(1, 7):
        tmp += i
        if(tmp >= num):
            return i
        
video_num = int(input().strip())
if video_num <= 21:
    print(my_sum(video_num))
else: print((video_num+27)//7)