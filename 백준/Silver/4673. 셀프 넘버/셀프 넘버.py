def self(num):
	total = num
	while num != 0:
		total += num % 10
		num //= 10
	return total

A = set()
B = set()

for i in range(1,10001):
  A.add(i)
  n = self(i)
  B.add(n)

selfnum = sorted(A-B)

for i in selfnum:
  print(i)