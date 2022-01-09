#Time: O(E+V), Space : O(E+V)
def bfs(root,adj):
    seen_level = {root:0}
    parent = {root:None}
    curent_level= 1
    current_nodes = [root]
    
    while current_nodes:
        next = []
        for u in current_nodes:
            print(str(u) + " Level: " + str(seen_level[u]))
            for v in adj[u]:
                if v not in seen_level:
                    seen_level[v] = current_level
                    parent[v] = u
                    next.append(v)

        current_nodes = next
        current_level += 1

adjacency = {1:[2,3,4],2:[],3:[], 4:[5,6],5:[],6:[]}

bfs(1,adjacency)
