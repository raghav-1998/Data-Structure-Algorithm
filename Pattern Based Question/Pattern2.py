"""
Ex:1

Input: n=3

Output:

111
222
333

Ex:2

Input: n=5

Output:

11111
22222
33333
44444
55555

"""

def pattern2(n):
    for i in range(1,n+1):
        for j in range(n):
            print(i,end="")
        print()

if __name__=="__main__":
    n=int(input())
    pattern2(n)