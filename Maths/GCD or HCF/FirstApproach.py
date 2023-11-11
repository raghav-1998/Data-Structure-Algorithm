
def gcd(a,b):
    ans=1
    for i in range(2,min(a,b)+1):
        if(a%i==0 and b%i==0):
            ans=i
        
    return ans
if __name__=="__main__":
    #Enter 2 numbers in space separated form
    a,b=[int(i) for i in input().strip().split(' ')]
    print("GCD of",a,"&",b,"is",gcd(a,b))