import sys
input = sys.stdin.readline

test_case = int(input().strip())
for _ in range(test_case):
    a, b, c, d, e = map(int, input().strip().split())
    a *= 350.34
    b *= 230.90
    c *= 190.55
    d *= 125.30
    e *= 180.90
    print(f"${sum((a, b, c, d, e)):.2f}")