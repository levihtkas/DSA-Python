def mergeSort(arr,si,ei):
  if si>=ei:
    return
  mid_index = (si+ei)//2
  mergeSort(arr,si,mid_index)
  mergeSort(arr,mid_index+1,ei)

  return merge(arr,si,mid_index,ei)

def merge(arr,si,mid_index,ei):
  temp=[]
  i = si
  j= mid_index+1
  while i<=mid_index and j<=ei:
    if arr[i]<arr[j]:
      temp.append(arr[i])
      i+=1
    else:
      temp.append(arr[j])
      j+=1
  while i <= mid_index:
    temp.append(arr[i])
    i+=1
  while j<ei:
    temp.append(arr[j])
    j+=1
  for idx, val in enumerate(temp):
    arr[si + idx] = val



arr= [33,12,122,54,222,1256]
temp = mergeSort(arr,0,len(arr)-1)
print(arr)