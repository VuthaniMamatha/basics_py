n=5
for i in range(0,5):
  for j in range(n-i):
    print(' ',end=' ')
  for j in range(i+1):
    print('*',end=' ')
  for j in range(i):
    print('*',end=' ')
  print()
