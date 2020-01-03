def getClosest(distance,visited,n):

    minDist = float('inf') - 1
    minDistIndex = 0

    for i in range(n):
        if distance[i] < minDist and not visited[i]:
            minDist = distance[i]
            minDistIndex = i

    return minDistIndex

def printPath(path,j):
    if path[j] == -1:
        print(j)
        return
    printPath(path,path[j])
    print(j)
    
def djikstra(adj_matrix,src):

    n = len(adj_matrix)
    visited = [False] * n
    path = [-1] * n
    distance = [float('inf')] * n

    distance[src] = 0


    for i in range(n):
        
        nearest =  getClosest(distance,visited,n)
        print(distance,nearest,end='\n')
        visited[nearest] = True

        for j in range(n):
            if adj_matrix[nearest][j] > 0 and not visited[j]  and distance[j] > distance[nearest] + adj_matrix[nearest][j]:
                distance[j] = distance[nearest] + adj_matrix[nearest][j]
                path[j] = nearest 

    print(distance,end='\n')
    
    for i in range(1,n):
        printPath(path,i)
        print('\n')
            
        
if __name__ == '__main__':
    
    adj_matrix = [  [0, 4, 0, 0, 0, 0, 0, 8, 0], 
                    [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                    [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                    [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                    [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                    [0, 0, 4, 14, 10, 0, 2, 0, 0], 
                    [0, 0, 0, 0, 0, 2, 0, 1, 6], 
                    [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                    [0, 0, 2, 0, 0, 0, 6, 7, 0] 
                 ]

    djikstra(adj_matrix,0)
