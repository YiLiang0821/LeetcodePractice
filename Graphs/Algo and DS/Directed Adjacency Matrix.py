class Graph:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes + 1
        self.graph = [[0 for _ in range(self.numberOfNodes)] for _ in range(self.numberOfNodes)]

    # check bound
    def withInBound(self, v1, v2):
        return ((0 <= v1 and v1 <= self.numberOfNodes)\
            and (0 <= v2 and v2 <= self.numberOfNodes))
    def insertEdge(self, v1 ,v2):
        if self.withInBound(v1, v2):
            self.graph[v1][v2] = 1
    def printGraph(self):
        for node in range(self.numberOfNodes):
            for v in range(len(self.graph[node])):
                if self.graph[node][v]:
                    print(node, '->', v)

g = Graph(5)
print(g.graph)
g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)
print(g.graph)
g.printGraph()