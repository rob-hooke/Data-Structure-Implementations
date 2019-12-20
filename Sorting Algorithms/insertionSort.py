def insertionSort(arr):
    n = len(arr)
    
    for i in range(1,n):

        hole = i
        value = arr[hole]
        #print(hole)
        
        while value < arr[hole - 1] and hole > 0:
            arr[hole] = arr[hole - 1]
            hole -= 1

        arr[hole] = value
        #print(arr)

arr = [5,4,3,2,1,6,7,8,9,10]

insertionSort(arr)

print(arr)
            
        

        
