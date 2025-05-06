import sys
input = sys.stdin.readline

music = list(map(str, input().strip().split("|")))
C_major = set(['C', 'F', 'G'])
A_minor = set(['A', 'D', 'E'])
C_count, A_count = 0, 0
for i in range(len(music)):
    if music[i][0] in C_major: C_count += 1
    elif music[i][0] in A_minor: A_count += 1

if C_count > A_count: print("C-major")
elif C_count < A_count: print("A-minor")
else:
    if music[-1][-1] in C_major: print("C-major")
    else: print("A-minor")