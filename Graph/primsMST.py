def printPrims(parent,adjacency_matrix):

    for c in range(1,len(adjacency_matrix)):

        print(f'{c} - {parent[c]}  {adjacency_matrix[c][ parent[c] ]}')
        print('\n')

def getClosest(key,mst):
    m = float('inf') - 1
    mIndex = -1

    for i in range(len(key)):
        if not mst[i] and key[i] < m:
            m = key[i]
            mIndex = i

    return mIndex


def prims(adjacency_matrix,src):
    vertices = len(adjacency_matrix)

    mst = [False] * vertices
    key = [float('inf') - 1] * vertices
    key[src] = 0

    parent = [None] * vertices
    parent[0] = -1

    for _ in range(vertices):

        u = getClosest(key,mst)
        mst[u] = True

        for _i in range(vertices):
            if adjacency_matrix[u][_i] > 0 and not mst[_i] and key[_i] > adjacency_matrix[u][_i]:
                key[_i] = adjacency_matrix[u][_i]
                parent[_i] = u

    printPrims(parent,adjacency_matrix)
                
if __name__ == '__main__':
    
    adjacency_matrix = [ [0, 2, 0, 6, 0], 
                         [2, 0, 3, 8, 5], 
                         [0, 3, 0, 0, 7], 
                         [6, 8, 0, 0, 9], 
                         [0, 5, 7, 9, 0]
                       ]

    prims(adjacency_matrix,0)
    
