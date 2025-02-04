from collections import defaultdict, deque

def graph_to_matrix(edges, n_nodes):
    matrix = [[0] * n_nodes for _ in range(n_nodes)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
    return matrix

def print_matrix(matrix):
    print("Ma trận kề:")
    for row in matrix:
        print(" ".join(map(str, row)))

def create_adj_list(matrix):
    adj_list = defaultdict(list)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i + 1].append(j + 1)
    return adj_list

def weakly_connected_components(matrix):
    adj_list = create_adj_list(matrix)
    undir_adj_list = defaultdict(list)
    for u in adj_list:
        for v in adj_list[u]:
            undir_adj_list[u].append(v)
            undir_adj_list[v].append(u)

    visited = set()
    weakly_count = 0

    def bfs(node):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in undir_adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            weakly_count += 1
            visited.add(node)
            bfs(node)

    return weakly_count

def strongly_connected_components(matrix):
    adj_list = create_adj_list(matrix)

    visited = set()
    finish_stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
        finish_stack.append(node)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            dfs(node)

    reversed_adj_list = defaultdict(list)
    for u in adj_list:
        for v in adj_list[u]:
            reversed_adj_list[v].append(u)

    visited.clear()
    strongly_connected_count = 0

    def dfs_reversed(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in reversed_adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            strongly_connected_count += 1
            dfs_reversed(node)

    return strongly_connected_count


if __name__ == "__main__":
    edges = [
        (1, 2), (1, 4), (2, 3), (2, 6),
        (6,3), (6, 4), (5,4), (7, 6),
        (7,3), (7, 5), (7, 8), (8,9), (5,9)
    ]
    n_nodes = 9

    G = graph_to_matrix(edges, n_nodes)

    print_matrix(G)

    weakly_connected = weakly_connected_components(G)
    strongly_connected = strongly_connected_components(G)

    print("\nWeak Connected Component's number:", weakly_connected)
    print("Strong Connected Component's number:", strongly_connected)