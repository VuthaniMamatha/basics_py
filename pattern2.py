n=4
for i in range(0,4):
  for j in range(n-i):
    print(' ',end='')
  for j in range(i+1):
    print('*',end='')
  print()
