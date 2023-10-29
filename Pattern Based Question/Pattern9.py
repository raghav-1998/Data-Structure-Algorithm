"""
Ex:1

Input: n=3

Output:

1
23
345

Ex:2

Input: n=4

Output:

1
23
345
4567

"""

def pattern9(n):
    for row in range(1,n+1):
        for col in range(row):
            print(row+col,end="")
        print()
        
if __name__=="__main__":
    n=int(input())
    pattern9(n)