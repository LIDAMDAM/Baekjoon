import sys
input = sys.stdin.readline

N = int(input().strip())
size_num = list(map(int, input().strip().split()))
T, P = map(int, input().strip().split())
total_t = 0

for i in size_num:
    total_t += i//T + (1 if i%T > 0 else 0)


print(total_t)
print(N//P, N%P)