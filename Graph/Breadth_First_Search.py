from collections import deque
def bfs(adjacency,root):
    qu = deque()

    visited = dict()

    qu.append(root)
    visited[root] = 1

    while len(qu) != 0:

        curr = qu.popleft()

        print(curr)

        for node in adjacency[curr]:
            if node not in visited:
                qu.append(node)
                visited[node] = 1
    



adjacency = {'a': ['b','c','d'],
             'b': ['a','e'],
             'c': ['a','e'],
             'd': ['a','e'],
             'e': ['b','c','d']
             
    }


bfs(adjacency,'a')
