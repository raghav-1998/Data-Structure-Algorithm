
def bubbleSort(arr,n):
    for i in range(n-1):
        print("Pass",i+1,":")
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(arr)


if __name__=="__main__":
    arr=[14,10,12,22,21]
    #arr=[1,2,3,4,5]
    n=len(arr)
    print("Array Before Sorting:",arr)
    bubbleSort(arr,n)
    print("Array After Sorting:",arr)
