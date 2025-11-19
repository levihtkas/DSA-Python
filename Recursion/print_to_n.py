def print_to_n(n):
  if(n==0):
    return 
  print_to_n(n-1)
  print(n)

def print_n_to_1(n):
  if(n==0):
    return 
  print(n)
  print_n_to_1(n-1)

# print_to_n(10)
print_n_to_1(10)