def quickSort(arr,start,end):
    if start >= end:
        return
    
    pIndex = partition(arr,start,end)
    print(pIndex)
    quickSort(arr,start,pIndex - 1)
    quickSort(arr,pIndex+1,end)

def partition(arr,start,end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex += 1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return pIndex


arr = [5,4,3,2,1]
quickSort(arr,0,len(arr) - 1)
print(arr)
     
