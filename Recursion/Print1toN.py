"""
I/P: N=5
O/P: 1 2 3 4 5

f(5)=f(4) 5
f(4)=f(3) 4
f(3)=f(2) 3
f(2)=f(1) 2
f(1)=f(0) 1
Constraint: N>=1
"""

def print1toN(n):
    if n==0:
        return
    print1toN(n-1)
    print(n, end=" ")

if __name__=="__main__":
    n=int(input())
    print1toN(n)
