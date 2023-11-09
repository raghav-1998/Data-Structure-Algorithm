
def selectionSort(arr,n):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        print("Pass",i,":",arr)

if __name__=="__main__":
    arr=[64,25,12,22,11]
    n=len(arr)
    selectionSort(arr,n)
    print("Sorted Array:",arr)