def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return

    mid = int(n/2)
    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l)
    mergeSort(r)

    merge(l,r,arr)



def merge(left,right,arr):

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        elif left[i] > right[j]:
            arr[k] = right[j]
            j += 1
            k += 1


    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        j += 1




arr = [5,4,3,2,1]

mergeSort(arr)

print(arr)
