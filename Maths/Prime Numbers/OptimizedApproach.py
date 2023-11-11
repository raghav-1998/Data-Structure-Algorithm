import math as m
def checkPrime(n):
    for i in range(2,int(m.sqrt(n))+1):
        if(n%i==0):
            return False
    
    return True

if __name__=="__main__":
    n=int(input())
    if checkPrime(n):
        print(n,"is a Prime Number")
    else:
        print(n,"is not Prime Number")