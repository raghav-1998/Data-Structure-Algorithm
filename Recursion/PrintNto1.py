"""
I/P: N=5
O/P: 5 4 3 2 1
5 f(4)
Constraint: N>=1
"""
import sys
sys.setrecursionlimit(100000)

def printNto1(n):
    if(n==0):
        return
    print(n,end=' ')
    printNto1(n-1)

if __name__=="__main__":
    n=int(input())
    printNto1(n)