"""
Ex:1

Input: n=3

Output:

1
22
333

Ex:2

Input: n=5

Output:

1
22
333
4444
55555

"""

def pattern7(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()
    
    
if __name__=="__main__":
    n=int(input())
    pattern7(n)