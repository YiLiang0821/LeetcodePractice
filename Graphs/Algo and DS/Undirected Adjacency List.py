from typing import DefaultDict
class Graph:
    def __init__(self):
        self.graph = DefaultDict(list)

    def insetEdge(self, v1, v2):
        # v1 will point to v2
        self.graph[v1].append(v2)

        # v2 also relation with v2
        self.graph[v2].append(v1)
    def printGraph(self):
        #key
        for node in self.graph:
            value = ''.join(str(self.graph[node]))
            print('{}=>{}'.format(node, value))
            # value in the list
            # for v in self.graph[node]:
            #     print('{}=>{}'.format(node, v))
'''
v1 point to v2, v3, v4
v2 -> v1
v3 -> v1
v4 -> v1
'''
g = Graph()
g.insetEdge(1, 5)
g.insetEdge(1, 100)
g.insetEdge(5, 2)
g.insetEdge(2, 7)
g.insetEdge(2, 200)
g.insetEdge(7, 1)
g.printGraph()