class minHeapNode:
    def __init__(self,num,arrNo,nextElem):
        self.val = num
        self.i = arrNo
        self.j = nextElem
        
class heapDS:
    #arr = []
    #size = 0
    def __init__(self,total):
        self.arr = []
        self.size = 0
        #self.capacity = total
    
    def addElement(self,node):
        self.arr.append(node)
        self.size += 1
        self.heapifyUp()

    def delMin(self):
        self.arr[0] = self.arr[self.size - 1]
        self.arr = self.arr[:-1]
        self.size -= 1
        self.heapifyDown()

        
    
    def heapifyUp(self):
        i = self.size - 1   
        flag = True
        while flag:
            parent = int((i - 1) / 2)
            
            if parent < 0:
                flag = False
                break                
            if self.arr[parent].val > self.arr[i].val:
                self.arr[parent],self.arr[i] = self.arr[i],self.arr[parent]
                i = parent
            else:
                flag= False       

    def heapifyDown(self):
        i = 0
        flag = True
        while flag:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= self.size:
                flag = False
                break
            elif right >= self.size:
                minC = left

            else:
                minC = left if self.arr[left].val < self.arr[right].val else right            
            

            if self.arr[minC].val < self.arr[i].val :
                self.arr[minC],self.arr[i] = self.arr[i],self.arr[minC]
                i = minC
            else:
                flag = False
                       

    def peek(self):
        return self.arr[0]


if __name__ == '__main__':
    A = [[1,5,9,13],
         [2,9,10,20,25],
         [3,7,11,15],
         [4,8,12,16]]

    obj = heapDS(len(A))

    for i in range(len(A)):
        temp_node = minHeapNode(A[i][0],i,1)
        obj.addElement(temp_node)

    while obj.size != 0:
        curr_min = obj.peek()
        print(curr_min.val)
        obj.delMin()
        delRow = curr_min.i
        nxtAdd = curr_min.j

        if nxtAdd < len(A[delRow]):
            obj.addElement(minHeapNode(A[delRow][nxtAdd],delRow,nxtAdd + 1))
        
        

    

    #Output : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
