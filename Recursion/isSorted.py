def isSorted(a):
  l = len(a)
  if l==0 or l==1:
    return True
  if a[0] > a[1]:
    return False
  return isSorted(a[1:])

print(isSorted([1,2,3]))

def isSortedBetter(arr,si):
  l = len(arr)
  if l==0:
    return True
  if si == l-1:
    return True
  if arr[si]>arr[si+1]:
    return False
  return isSortedBetter(arr,si+1)

print(isSortedBetter([1,26,3],0))