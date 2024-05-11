"""
Write a Program to find of number using recursion.

I/P: N=3
O/P: 6

"""

def factorial(n):
    if n==0:
        return 1

    return n*factorial(n-1)


if __name__=="__main__":
    n=int(input())
    print("Factorial of",n,"is ",factorial(n))