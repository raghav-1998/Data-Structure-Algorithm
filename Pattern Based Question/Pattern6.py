"""
Ex:1

Input: n=3

Output:

*
**
***

Ex:2

Input: n=5

Output:

*
**
***
****
*****

"""

def pattern6(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        
        print()


if __name__=="__main__":
    n=int(input())
    pattern6(n)
