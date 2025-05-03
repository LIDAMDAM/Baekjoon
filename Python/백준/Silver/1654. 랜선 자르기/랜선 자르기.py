import sys
input = sys.stdin.readline

lan_count, lan_need = map(int, input().strip().split())
lan_array = [int(input().strip()) for _ in range(lan_count)]

start = 1
end = max(lan_array)
result = 0

while(start <= end):
    mid = (start+end)//2
    total = sum(lan//mid for lan in lan_array)
    if total >= lan_need:
        result = mid
        start = mid + 1
    else: end = mid - 1

print(result)