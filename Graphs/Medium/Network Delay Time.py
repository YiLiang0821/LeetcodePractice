#743
# Dijkstra Algo
from typing import DefaultDict
import heapq

def networkDelayTime(times, n, k):
    #init graph
    g = DefaultDict(list)
    # u is the parent node
    # v is the node parent point to
    # w is the cost
    for u, v, w in times:
        g[u].append((w, v))

    pqueue = []
    heapq.heappush(pqueue, (0, k))
    seen = set()
    distance = {i: float('inf') for i in range(1, n+1)}
    distance[k] = 0

    while(pqueue):
        cur_dis, vertex = heapq.heappop(pqueue)
        seen.add(vertex)
        #  all the n nodes to receive the signal
        if len(seen) == n:
            return cur_dis
        # check distance of vertex's neighbor
        for cost, node in g[vertex]:
            if node not in seen and cur_dis + cost < distance[node]:
                distance[node] = cur_dis + cost
                heapq.heappush(pqueue, (distance[node], node))
    return -1



    
    

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))