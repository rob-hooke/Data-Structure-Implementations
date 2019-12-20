def selectionSort(arr):

    n = len(arr)

    for i in range(n):
        m = i
        for j in range(i+1,n):
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[m],arr[i] = arr[i],arr[m]

arr = [5,4,3,2,1,-20,-1,4,56,321,234,678,23,9]

selectionSort(arr)

print(arr)
    
