import sys
input = sys.stdin.readline

test_case = int(input().strip())
lank_array = []
inform_array = []
for _ in range(test_case):
    inform_array.append(list(map(int, input().split())))

for i in range(test_case):
    count = 0
    for j in range(test_case):
        if inform_array[i][0] < inform_array[j][0] and inform_array[i][1] < inform_array[j][1]:
            count += 1
    lank_array.append(count+1)

print(" ".join(map(str, lank_array)))