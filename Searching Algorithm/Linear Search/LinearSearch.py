
def search(arr,key):
    n=len(arr)

    for i in range(n):
        if(arr[i]==key):
            return i
    
    return -1

if __name__=="__main__":
    key=int(input())
    arr=[10,4,2,9,1,3,8,6,5,7]

    result=search(arr,key)

    if result==-1:
        print(key,"is not present in array")
    else:
        print(key,"is present at",result,"index in array")