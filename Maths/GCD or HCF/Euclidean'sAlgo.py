"""
This is the iterative version of Eucleidean Algo.
"""

def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    
    while(a!=b):
        if(a>b):
            a-=b
        else:
            b-=a
    
    return a

if __name__=="__main__":
    #Enter 2 numbers in space separated form
    a,b=[int(i) for i in input().strip().split(' ')]
    print("GCD of",a,"&",b,"is",gcd(a,b))