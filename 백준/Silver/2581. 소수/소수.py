M = int(input())
N = int(input())

L = []
test = 0

if M == 1:
    M = 2
for i in range(M, N+1):
    for j in range(2, i):
        if (i%j) == 0:
            test += 1
    if test == 0:
        L.append(i)
    test = 0

L.sort()

if(len(L)==0):
    print(-1)
else:
    print(sum(L))
    print(L[0])