import sys
input = sys.stdin.readline

chess_board = []
n, m = map(int, input().strip().split())
for _ in range(n):
    chess_board.append(list(input().strip()))
min_paint = 64

for x in range(n-7):
    for y in range(m-7):
        Bpaint_count = 0
        Wpaint_count = 0
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    if chess_board[i+x][j+y] == 'W':
                        Bpaint_count += 1
                    else: Wpaint_count += 1
                else:
                    if chess_board[i+x][j+y] == 'B':
                        Bpaint_count += 1
                    else: Wpaint_count += 1
        min_paint = min(Bpaint_count, Wpaint_count, min_paint)

print(min_paint)