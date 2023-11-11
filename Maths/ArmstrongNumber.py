
def checkArmstrong(n):
    digits=0
    temp=n
    original=n
    ans=0
    while(temp!=0):
        temp//=10
        digits+=1
    
    while(n!=0):
        ans+=((n%10)**digits)
        n//=10
    
    return original==ans

if __name__=="__main__":
    n=int(input())
    if(checkArmstrong(n)):
        print(n,"is a Armstrong Number")
    else:
        print(n,"is not an Armstrong Number")