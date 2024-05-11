"""
Write a program to check whether string is palindrome or not.

I/P: s="abba"
O/P: Yes

I/P: s="geeks"
O/P: No

"""

def checkPalindrome(s,start,end):
    if(start>=end):
        return True
    
    return s[start]==s[end] and checkPalindrome(s,start+1,end-1)

if __name__=="__main__":
    s=input()
    start=0
    end=len(s)-1
    if(checkPalindrome(s,0,end)):
        print("String is Palindrome")
    else:
        print("String is not Palindrome")