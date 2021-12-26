def BFS(graph, start):
    seen = set()
    queue = []
    queue.append(start)
    
    while (len(queue)):
        vertex = queue.pop(0)
        seen.add(vertex) # exist in q
        print(vertex, end=' ')
        for node in graph[vertex]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
    return 
graph = {1: [2, 3], 
        2: [4, 5],
        3: [5], 4: [6], 
        5: [6],
        6: [7], 
        7: []}
BFS(graph, 1)
'''
TC is O(V+E), V -> vertices(nodes), E -> edges
SC is O(V)
'''