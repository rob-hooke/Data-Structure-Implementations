def topSort(graph,visited,stack):

    for i in range(len(visited)):
        if visited[i] == False:
            topSortUtil(i + 1,graph,visited,stack)

    return stack


def topSortUtil(node,graph,visited,stack):

    neighbours = graph[node]
    visited[node-1] = True
    
    for n in neighbours:
        if visited[n-1] == False:
            topSortUtil(n,graph,visited,stack)

    stack.append(node)

    
if __name__ == '__main__':
    
    graph = {
             1:[3],
             2:[3,5],
             3:[4],
             4:[6],
             5:[6],
             6:[7],
             7:[]
            }

    visited = [False] * len(graph.keys())

    stack = []

    result = topSort(graph,visited,stack)

    print(result[::-1])
