import heapq

def adjacency_matrix():
    n = 10
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    edges = [
        (0, 1, 4), (0, 2, 1),
        (1, 5, 3),
        (2, 3, 8), (2, 5, 7),
        (3, 7, 5),
        (4, 8, 2), (4, 7, 2),
        (5, 4, 1), (5, 7, 1),
        (6, 8, 4), (6, 9, 4),
        (7, 6, 7), (7, 9, 7), (7, 8, 6),
        (8, 9, 1)
    ]
    for u, v, w in edges:
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w
    return adj_matrix

def show_adjacency_matrix(adj_matrix):
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(" ".join(f"{x if x != float('inf') else '∞':>3}" for x in row))

def dijkstra(adj_matrix, start, end):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    prev_nodes = [-1] * n
    min_heap = [(0, start)]
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] != float('inf'):
                new_distance = current_distance + adj_matrix[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    prev_nodes[neighbor] = current_node
                    heapq.heappush(min_heap, (new_distance, neighbor))
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = prev_nodes[node]
    path.reverse()
    return path, distances[end]

if __name__ == "__main__":
    adj_matrix = adjacency_matrix()
    show_adjacency_matrix(adj_matrix)
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
    start_node = input("\nEnter source node (A-M): ").upper()
    end_node = input("Enter target node (A-M): ").upper()
    start_index = nodes.index(start_node)
    end_index = nodes.index(end_node)
    shortest_path, shortest_distance = dijkstra(adj_matrix, start_index, end_index)
    print("\nShortest Path:", " -> ".join(nodes[node] for node in shortest_path))
    print("Weighted Sum of Shortest Path:", shortest_distance)