n, b = map(int, input().split())
r = ("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
s = ''

while n:
    s += str(r[n%b])
    n //= b

print(s[::-1])