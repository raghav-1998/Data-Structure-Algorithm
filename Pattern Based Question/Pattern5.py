"""
Ex:1

Input: n=3

Output:

123
456
789

"""

def pattern5(n):
    num=1
    for i in range(n):
        for j in range(n):
            print(num,end="")
            num+=1
        print()

if __name__=="__main__":
    n=int(input())
    pattern5(n)
