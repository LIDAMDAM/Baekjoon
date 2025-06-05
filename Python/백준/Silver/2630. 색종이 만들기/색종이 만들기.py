import sys
input = sys.stdin.readline

paper_size = int(input())
paper = [list(map(int, input().split())) for _ in range(paper_size)]
blue_count = 0
white_count = 0

def check(x, y, size):
    first = paper[x][y]
    if size == 1:
        return "Blue" if first == 1 else "White"
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first:
                return False
    return "Blue" if first == 1 else "White"

def count_paper(x, y, size):
    global blue_count, white_count
    tmp = check(x, y, size)

    if tmp == "Blue":
        blue_count += 1
        return
    elif tmp == "White":
        white_count += 1
        return
    else:
        half_size = size // 2
        count_paper(x, y, half_size)
        count_paper(x + half_size, y, half_size)
        count_paper(x, y + half_size, half_size)
        count_paper(x + half_size, y + half_size, half_size)

count_paper(0, 0, paper_size)
print(white_count, blue_count, sep='\n')