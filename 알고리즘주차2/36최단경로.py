import sys
from collections import defaultdict
import heapq

graph = defaultdict(dict)

V,E = map(int,input().split())
start_node = int(input())

#그래프 만들기
for _ in range(E):
    current_node,adjacent_node,weight = map(int,sys.stdin.readline().split())
    if graph[current_node].get(adjacent_node)!=None:
        graph[current_node][adjacent_node]=min(graph[current_node][adjacent_node],weight)
    else:
        graph[current_node][adjacent_node]=weight


def dijkstra(graph,start_node):
    #초기화    
    distances = {node : float('inf') for node in range(1,V+1)}
    distances[start_node] = 0
    queue = []
    heapq.heappush(queue,(distances[start_node],start_node))
    

    while queue:
        current_distance,current_node=heapq.heappop(queue)
        
        #현재가 최단경로라는 뜻 이므로 할필요가 없음
        if distances[current_node] < current_distance:
            continue
        
        #현재가 최단경로가 아니므로 갱신이 필요
        for adjacent_node,weight in graph[current_node].items():
            #최단경로 갱신하는 것 
            renewed_distance = current_distance+weight
            if distances[adjacent_node] > renewed_distance:
                distances[adjacent_node] = renewed_distance
                heapq.heappush(queue,(renewed_distance,adjacent_node))
                
    return distances


shortest_path=dijkstra(graph,start_node)

for node,distance in shortest_path.items():
    if distance==float('inf'):
        print("INF")
        continue
    print(distance)