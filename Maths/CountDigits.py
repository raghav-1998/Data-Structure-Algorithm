
def countDigits(n):
    ans=0
    while(n!=0):
        n//=10
        ans+=1
    
    return ans

if __name__=="__main__":
    n=int(input())
    count_digits=countDigits(n)
    print("Number of digits in",n,"is",count_digits)