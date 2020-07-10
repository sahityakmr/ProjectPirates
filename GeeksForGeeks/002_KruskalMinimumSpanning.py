class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def union(self,parent,rank,x,y):
        xRoot = self.find(parent,x)
        yRoot = self.find(parent,y)

        if rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot

        elif rank[yRoot] > rank[xRoot]:
            parent[xRoot] = yRoot

        else:
            parent[xRoot] = yRoot
            rank[yRoot] += 1

    def KruskalMST(self):
        result = []
        edgePointer = 0
        resultPointer = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while resultPointer < self.V-1:
            u,v,w = self.graph[edgePointer]
            edgePointer += 1

            x = self.find(parent,u)
            y = self.find(parent,v)

            if x!=y:
                resultPointer += 1
                result.append([u,v,w])
                self.union(parent,rank,x,y)

        print("Following are the edges in constructed MST")
        for u,v,weight in result:
            print("%d -- %d == %d" % (u,v,weight))

#Driver
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()

