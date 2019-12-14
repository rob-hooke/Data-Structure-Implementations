class DLL:
    def __init__(self,x,key):
        self.value = x
        self.keys = key
        self.prev = None
        self.next = None

size = 0
head,tail = None,None
lookup = dict() #key:DLL Node


def put_data(key,val):
    capacity = 5
    global size,head,tail,lookup
    if key in lookup:             #Updating if key is already present
        lookup[key].value = val
    else:      
        if size == capacity:
            temp = tail
            tail = tail.prev
            tail.next = None
            temp.prev = None
            del lookup[temp.keys] #deleting last used from hashtable
            
            temp = DLL(val,key)   #creating he new node
            temp.next = head
            head = temp            
        elif size == 0:
            temp = DLL(val,key)
            head,tail = temp,temp
            size += 1
        else:
            temp = DLL(val,key)
            temp.next = head
            head.prev = temp
            head = temp
            size += 1
            

        lookup[key] = temp


def get_data(key):

    if key in lookup:
        return lookup[key].value
    else:
        return None
    




if __name__ == '__main__':
    
    put_data(1,1)
    put_data(2,2)
    put_data(3,3)
    put_data(4,4)
    put_data(5,5)
    print(get_data(3))
    print(get_data(5))
    put_data(5,10)
    print(get_data(5))
    put_data(6,15)
    print(get_data(1))
