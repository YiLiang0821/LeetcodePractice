graph = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D'],
    'C':['A', 'B', 'D', 'E'],
    'D':['B', 'C', 'E', 'F'],
    'E':['C', 'D'],
    'F':['D']
}

def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start) # exist in q
    parent = {} # record father node
    parent[start] = None # inital node

    while (len(queue) > 0):
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        #print(vertex)
    return parent
shortCut = BFS(graph,'E')
print(shortCut)
for s in shortCut:
    print(s, shortCut[s])
'''
inputValue = input('finde the shotcut from E to \n')
while (inputValue != None):
    print(inputValue)
    inputValue = shortCut[inputValue]
'''