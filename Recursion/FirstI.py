def firstIndex(arr, x):
    # Please add your code here
    if arr[0]==x:
        return 0
    elif len(arr) == 1:
        return -1
    smallOutput =firstIndex(arr[1:],x)
    if smallOutput==-1:
        return -1
    return 1+smallOutput

def firstIndexes(arr,x,si):
    if arr[si]==x:
        return si
    if si==len(arr)-1:
        return -1
    smallO=firstIndexes(arr,x,si+1)
    if smallO==-1:
        return -1
    else: 
        return smallO



n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndexes(arr, x,0))
