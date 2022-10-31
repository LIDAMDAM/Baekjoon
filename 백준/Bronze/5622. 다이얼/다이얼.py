eng = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = int(0)
for i in eng:
  for j in i:
    for h in word:
      if j == h:
        time += eng.index(i) + 3
print(time)