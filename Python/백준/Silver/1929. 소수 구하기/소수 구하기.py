import sys
input = sys.stdin.readline

min_num, max_num = map(int, input().strip().split())
prime_num = [True for i in range(max_num+1)]
prime_num[0], prime_num[1] = False, False

for i in range(2, int(max_num**0.5)+1):
    if prime_num[i]:
        for j in range(i*i, max_num+1, i):
            prime_num[j] = False

for i in range(min_num, max_num+1):
    if prime_num[i]:
        print(i)