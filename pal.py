def pal(a):
  for i in range(2,a):
    if a%i==0:
      return False
  return True
pal(9)
