# A = Root node

while A != None:
            if A.left == None:
                print(A.val) #res.append(A.val)
                A = A.right
            
            else:
                
                pred =  A.left
                
                while pred.right != None and pred.right != A:
                    pred = pred.right
                    
                if pred.right == None:
                    pred.right = A
                    A = A.left
                else:
                    A = pred.right
                    pred.right = None
                    #A.left = None
                    print(A.val) #res.append(A.val)
                    A = A.right
