from operator import itemgetter
class graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])


    def find_parent(self,parent,node):
        if parent[node] == -1:
            return node
        if parent[node] != -1:
            return self.find_parent(parent,parent[node])

    def union(self,node1,node2,parent):
        node1_addr = self.find_parent(parent,node1)
        node2_addr = self.find_parent(parent,node2)
        parent[node1] = node2
      

    def kruskals(self):
        parent = [-1] * self.V
        result = []

        edges = 0
        present_edge = 0

        

        self.graph = sorted(self.graph,key = itemgetter(2))

        while edges < self.V - 1:

            u,v,w = self.graph[present_edge]

            u_add = self.find_parent(parent,u)
            v_add = self.find_parent(parent,v)

            if u_add != v_add:
                result.append([u,v,w])
                edges += 1
                self.union(u,v,parent)

            present_edge += 1

        print(result)
                
if __name__ == '__main__':
    g = graph(4)
    g.addEdge(0,1,10)
    g.addEdge(0,2,6)
    g.addEdge(0,3,5)
    g.addEdge(1,3,15)
    g.addEdge(2,3,4)

    g.kruskals()
