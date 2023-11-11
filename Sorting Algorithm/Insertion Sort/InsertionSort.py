
def insertionSort(arr,n):
    for i in range(1,n):
        temp=arr[i]
        j=i-1

        print("Pass",i,":")
        while(j>=0):
            if(arr[j]>temp):
                #Shift value to next position
                arr[j+1]=arr[j]
                j-=1
                print(arr)
            else:
                #Break the pass as element is arr[j] is at its correct position
                print(arr)
                break
        #As arr[j] is at correct position, so next position will be correct position for temp.
        arr[j+1]=temp
        print("After Pass",i,":",arr)

if __name__=="__main__":
    arr = [12, 11, 13, 5, 6]
    n=len(arr)
    print("Before Sorting:",arr)
    insertionSort(arr,n)
    print("After Sorting:",arr)
