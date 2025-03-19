n = int(input())

y, m = 2024, 1

m = m+n*7
if m > 12:
    y += m//12
    m = m % 12
    if m == 0:
        m += 12
        y -= 1

print(f"{y} {m}")