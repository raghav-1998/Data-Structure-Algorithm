
def checkPalindrome(n):
    x=n
    rev=0
    while(x!=0):
        rev=(rev*10)+(x%10)
        x//=10
    return n==rev

if __name__=="__main__":
    n=int(input())
    if(checkPalindrome(n)):
        print(n,"is a Palindrome Number")
    else:
        print(n,"is not Palindrome Number")