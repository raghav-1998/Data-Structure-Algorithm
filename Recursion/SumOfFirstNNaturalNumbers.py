"""
Write a Program to find sum of first N natural numbers using Recursion.

I/P: N=5
O/P: 15

1+2+3+4+5=f(4)+5
f(4)=f(3)+4
f(3)=f(2)+3
f(2)=f(1)+2

"""

def getSum(n):
    if(n==1):
        return 1
    return getSum(n-1)+n


if __name__=="__main__":
    n=int(input())
    print("Sum of First",n,"natural number is",getSum(n))