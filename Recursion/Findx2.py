def replaceX(s,a,b):
  if len(s)==0:
    return s
  
  smallOutput = replaceX(s[1:],a,b)
  if s[0] ==a:
    return b+smallOutput
  else:
    return s[0]+smallOutput


print(replaceX("sakthi","a","u"))