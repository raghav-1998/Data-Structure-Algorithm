def binarySearch(arr,length,key):
    start=0
    end=length-1
    mid=start+(end-start)//2

    while(start<=end):
        print("start:",start,"end:",end,"mid:",mid)
        if(arr[mid]==key):
            print("Mid value is:",arr[mid])
            return mid
        elif(arr[mid]>key):
            print("Mid value:",arr[mid],"is greater than",key,". So move to left side of array.")
            end=mid-1
        else:
            print("Mid value:",arr[mid],"is less than",key,". So move to right side of array.")
            start=mid+1
        
        mid=start+(end-start)//2
    
    return -1

if __name__=="__main__":
    key=int(input())
    oddArr=[1,2,3,4,5,6,7]
    evenArr=[10,20,30,40,50,60,70,80]

    oddResult=binarySearch(oddArr,len(oddArr),key)
    if oddResult==-1:
        print(key,"is not present in array")
    else:
        print(key,"is present at",oddResult,"index")

    evenResult=binarySearch(evenArr,len(evenArr),key)
    if evenResult==-1:
        print(key,"is not present in array")
    else:
        print(key,"is present at",evenResult,"index")
    

    