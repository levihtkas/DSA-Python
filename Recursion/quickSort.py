def pivotIndex(arr,si,ei):
  pivot = arr[si]
  count=0
  for i in range(si,ei):
    if arr[i] < pivot:
      count+=1
  arr[si+count],arr[si] = arr[si],arr[si+count]
  i=si
  j=ei-1
  while i < j:
    if arr[i] < arr[si+count]:
      i+=1
    elif arr[j] > arr[si+count]:
      j=j-1
    else:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j-=1
  return si+count
def quickSort(arr,si,ei):
  # print(si)
  if si >= ei:
    return 
  p = pivotIndex(arr,si,ei)
  quickSort(arr,si,p)
  quickSort(arr,p+1,ei)


leng=len([1,2,33,44,556,667,1234])
print(leng)
arr=[1,2,44,556,667,1234,33]
quickSort(arr,0,leng)

print(arr)


