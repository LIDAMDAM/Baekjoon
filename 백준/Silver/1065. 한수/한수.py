A = int(input())
count = int(0)

for i in range(1, A+1):
    a_3 = i//100
    a_2 = (i//10)%10
    a_1 = i%10
    if i//100 == 0:
        count += 1
    elif (a_3-a_2) == (a_2-a_1):
        count += 1
print(count)