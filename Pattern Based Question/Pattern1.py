"""
Ex:1

Input: n=3

Output:

***
***
***

Ex:2

Input: n=5

Output:

*****
*****
*****
*****
*****

"""

def pattern1(n):

    for i in range(n):
        for j in range(n):
            print("*",end='')
        
        print()

if __name__=="__main__":
    n=int(input())
    pattern1(n)