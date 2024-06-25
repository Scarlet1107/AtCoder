import heapq

# 隣接行列の定義
graph = [
    [99999, 10, 12, 2, 4, 99999, 99999, 99999, 3, 14, 99999],
    [10, 99999, 1, 99999, 99999, 99999, 99999, 99999, 99999, 7, 99999],
    [12, 1, 99999, 99999, 99999, 99999, 99999, 99999, 8, 99999, 99999],
    [2, 99999, 99999, 99999, 5, 3, 99999, 4, 3, 99999, 99999],
    [4, 99999, 99999, 5, 99999, 5, 10, 99999, 99999, 11, 10],
    [99999, 99999, 99999, 3, 5, 99999, 2, 4, 99999, 99999, 99999],
    [99999, 99999, 99999, 99999, 10, 2, 99999, 99999, 99999, 99999, 8],
    [99999, 99999, 99999, 4, 99999, 4, 99999, 99999, 5, 99999, 99999],
    [3, 99999, 8, 3, 99999, 99999, 99999, 5, 99999, 99999, 99999],
    [14, 7, 99999, 99999, 11, 99999, 99999, 99999, 99999, 99999, 7],
    [99999, 99999, 99999, 99999, 10, 99999, 8, 99999, 99999, 7, 99999]
]

def dijkstra(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_cost = [99999] * num_vertices
    min_cost[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_cost, current_vertex = heapq.heappop(priority_queue)
        
        if visited[current_vertex]:
            continue
        
        visited[current_vertex] = True
        
        for neighbor in range(num_vertices):
            cost = graph[current_vertex][neighbor]
            if cost != 99999 and not visited[neighbor]:
                new_cost = current_cost + cost
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
    
    return min_cost

# 頂点 A (頂点 0) からの最短経路木
start_vertex = 0
shortest_paths = dijkstra(graph, start_vertex)
print(f"頂点 {start_vertex} から各頂点への最小コスト: {shortest_paths}")
