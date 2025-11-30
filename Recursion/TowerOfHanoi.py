def TowerOfHanoi(n,a,b,c):

  if n == 1:
    print(a+" to "+c)
    return
  TowerOfHanoi(n-1,a,c,b)
  print(a+" to "+c)
  TowerOfHanoi(n-1,b,a,c)



TowerOfHanoi(3,"a","b","c")