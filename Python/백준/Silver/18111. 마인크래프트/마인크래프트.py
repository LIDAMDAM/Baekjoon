import sys
input = sys.stdin.readline

y, x, block_count = map(int, input().split())
ground = [0]*257
for _ in range(y):
    for i in map(int, input().split()): ground[i] += 1

time, high = float('inf'), 0
for i in range(257):
    if ground[i] > 0: min_val = i; break
for i in range(256, -1, -1):
    if ground[i] > 0: max_val = i; break

for i in range(min_val, max_val+1):
    block_tmp = block_count
    time_tmp = 0
    for index, value in enumerate(ground):
        if value == 0: continue
        dig_num = index - i
        if dig_num > 0:
            block_tmp += value*dig_num
            time_tmp += value*dig_num*2
        else:
            block_tmp += value*dig_num
            time_tmp -= value*dig_num
    if block_tmp < 0: continue
    if time_tmp < time or (time_tmp == time  and i  > high):
        time, high = time_tmp, i

print(time, high)