## Read input as specified in the question.
## Print output as specified in the question.
s=input()
start=0
end=len(s)-1
def checkPalindrome(s,start,end):
    if start>=end:
        return True
    if s[start] ==s[end]:
        return checkPalindrome(s,start+1,end-1)
    else:
        return False

result = checkPalindrome(s,start,end)
if result is True:
    print("true")
elif result is False:
    print("false")