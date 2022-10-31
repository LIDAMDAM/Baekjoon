s = input()
eng = 'abcdefghijklmnopqrstuvwxyz'
for i in eng:
  if i in s:
    print(s.index(i), end = ' ')
  else:
    print('-1', end = ' ')