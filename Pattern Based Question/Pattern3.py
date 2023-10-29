"""
Ex:1

Input: n=3

Output:

123
123
123

Ex:2

Input: n=5

Output:

12345
12345
12345
12345
12345

"""

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end="")
        
        print()
        

if __name__=="__main__":
    n=int(input())
    pattern3(n)