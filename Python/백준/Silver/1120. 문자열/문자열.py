import sys
input = sys.stdin.readline

string_A, string_B = map(str, input().strip().split())
max_count = 0
for j in range(len(string_B)-len(string_A)+1):
    count = 0
    for i in range(len(string_A)):
        if (string_B[i+j] == string_A[i]): count += 1
    if (max_count < count): max_count = count
print(len(string_A) - max_count)