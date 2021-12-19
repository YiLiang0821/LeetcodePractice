def DFS(graph, start):
    stack = []
    stack.append(start)
    seen = set()

    while (len(stack)):
        vertex = stack.pop()
        seen.add(vertex) # exist in q
        for node in graph[vertex]:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex, end=' ')

graph = {1: [2, 3], 
        2: [4, 5],
        3: [5], 4: [6], 
        5: [6],
        6: [7], 
        7: []}
DFS(graph,1)

'''
TC is O(V+E), V -> vertices(nodes); E -> Edges
SC is O(V)
'''