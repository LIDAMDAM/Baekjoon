a = []
m = int(input())
a.extend(map(int, input().split()))
print(sum(a)/max(a)*100/len(a))