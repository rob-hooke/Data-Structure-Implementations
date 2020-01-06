
    

def isCycleUtil(vertices,adjacency_list):

    parent = [-1] * vertices

    for i in range(vertices):
        for j in adjacency_list[i]:
            
            i_parent = findParent(parent,i)
            j_parent = findParent(parent,j)

            if i_parent == j_parent:
                return True
            union(i,j,parent)

            
    


def findParent(parent,node):
    if parent[node] == -1:
        return node
    if parent[node] != -1:
        return findParent(parent,parent[node])

def union(node1,node2,parent):
    #print(node1,node2)
    x = findParent(parent,node1)
    y = findParent(parent,node2)

    parent[x] = y
    
    #print(node1,node2,parent)

if __name__ == '__main__':

    adjacency_list = {
                        0:[1],
                        1:[2],
                        2:[0]        
                     }

    print('Cycle' if isCycleUtil(3,adjacency_list) else 'No Cycle')

    
    
