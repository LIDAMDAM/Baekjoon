import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
listen_p = [input().strip() for _ in range(n)]
show_p = set(input().strip() for _ in range(m))
result = sorted([name for name in listen_p if name in show_p])

print(len(result))
print("\n".join(result))