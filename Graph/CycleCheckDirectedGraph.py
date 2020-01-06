def cycleCheck(node,adjacency_list,visited,recStack):

    visited[node] = True
    recStack[node] = True
    

    neighbours = adjacency_list[node]

    for j in neighbours:
        if visited[j] == False:
            if cycleCheck(j,adjacency_list,visited,recStack) == True:
                return True
        else:
            if recStack[j] == True:
                return True
        
    recStack[node] = False
    return False



def isCycleUtil(vertices,adjacency_list):

    visited = [False] * vertices
    recStack = [False] * vertices

    for i in range(vertices):
        if visited[i] ==  False:
            if cycleCheck(i,adjacency_list,visited,recStack) == True:
                return True


    return False



if __name__ == '__main__':

    adjacency_list = {
                        0:[1,2],
                        1:[2],
                        2:[1]        
                     }

    print(isCycleUtil(3,adjacency_list))
    

    
