
def reverseNumber(n):
    ans=0
    while(n!=0):
        ans=(ans*10)+(n%10)
        n//=10
    
    return ans

if __name__=="__main__":
    n=int(input())
    reverse_number=reverseNumber(n)
    print("Reverse of number",n,"is",reverse_number)