import sys
input = sys.stdin.readline

entry = int(input().rstrip())
best_idx = 1
best_info = list(map(int, input().split()))
best_info = [best_info[0], -best_info[1], -best_info[2]]

for idx in range(2, entry+1):
    info = list(map(int, input().split()))
    info = [info[0], -info[1], -info[2]]
    if best_info < info: best_info, best_idx = info, idx

print(best_idx)