import heapq
import math

graph = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'C':2, 'D':1},
    'C':{'A':1, 'B':2, 'D':4, 'E':8},
    'D':{'B':1, 'C':4, 'E':3, 'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6}
}

def init_distance(graph, start):
    distance = {start: 0} # 當前點到起始點的距離
    for node in graph:
        if node != start:
            distance[node] = math.inf
    return distance

def dijkstra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    seen = set()
    parent = {start: None} # record father node
    distance = init_distance(graph, start)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dis = pair[0]
        vertex = pair[1]
        seen.add(vertex)  #when pop node -> be seen, since nodes can be put into pqueue many time
        nextNodes = graph[vertex].keys()
        for node in nextNodes:
            if node not in seen:
                if dis + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dis + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dis + graph[vertex][node]
        #print(vertex)
    return parent, distance



parent, distance = dijkstra(graph, 'A')
print(parent)
print(distance)

print('from A to F distans:', distance['F'])
s = 'F'
while(parent[s] != None):
    print(parent[s])
    s = parent[s]
'''
pls refer this video: https://www.youtube.com/watch?v=9wV1VxlfBlI
'''