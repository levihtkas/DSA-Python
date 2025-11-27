def replacePi(s):
  if len(s)==0 or len(s)==1:
    return s
  if s[0]=="p" and s[1] =="i":
    return "3.14"+replacePi(s[2:])
  else:
    return s[0]+replacePi(s[1:])
print(replacePi("ppiwdspi"))