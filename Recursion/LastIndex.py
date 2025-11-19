def LastIndex(arr,x):
  l= len(arr)
  if arr[l-1] == x:
    return l
  if(l==1):
    return -1
  smallO =LastIndex(arr[:-1],x)
  if smallO ==-1:
    return -1
  else:
    return smallO-1

arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(arr)
print(LastIndex(arr,x))