class heapDS:
    arr = []
    size = 0
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def addElement(self,val):

        self.arr.append(val)
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
            if i % 2 == 0:
                parent = int((i - 2) / 2)
            else:
                parent = int((i - 1) / 2)
            
            if parent < 0:
                flag = False
                break                
            if self.arr[parent] > self.arr[i]:
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
                minC = left if self.arr[left] < self.arr[right] else right            
            

            if self.arr[minC] < self.arr[i] :
                self.arr[minC],self.arr[i] = self.arr[i],self.arr[minC]
                i = minC
            else:
                flag = False
                       

    def peek(self):
        #print(self.arr)
        return self.arr[0]


obj = heapDS()

a = [4,2,7,6,5,1,10]

f = True
while f:
    inp = input('Enter number')
    if int(inp) == 0:
        break
    obj.addElement(int(inp))
    print(obj.peek())

        
