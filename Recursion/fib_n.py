#iterative solution

# n = int(input())
# x=1
# k=0
# count =0
# for i in range(n):
#   if i==0 or i==1:
#     print(i)
#     continue
#   if count ==n:
#     break
#   prev=x
#   x+=k
#   count+=1
#   print(x)
#   k=prev
  
def fib(n):
  if(n==1 or n==2):
    return n-1
  # print(n)
  return fib(n-1)+fib(n-2)
  

print(fib(5))
