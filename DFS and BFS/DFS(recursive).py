def dfs_recursive(graph, vertex, seen = []):
    seen += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in seen:
            dfs_recursive(graph, neighbor, seen)
    return seen
graph = {1: [2, 3], 
        2: [4, 5],
        3: [5], 4: [6], 
        5: [6],
        6: [7], 
        7: []}
print(dfs_recursive(graph, 1))
