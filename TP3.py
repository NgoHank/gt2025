def print_adjacency_matrix(adjacency_list):
    max_node = max(adjacency_list.keys())
    adj_matrix = [[0 for _ in range(max_node + 1)] for _ in range(max_node + 1)]

    for key in adjacency_list:
        for child in adjacency_list[key]:
            adj_matrix[key][child] = 1

    print("Adjacency Matrix:")
    for i in range(1, max_node + 1):
        print(" ".join(map(str, adj_matrix[i][1:])))


def inorder_traversal(node, adjacency_list, visited):
    if node is None or visited[node]:
        return

    visited[node] = True
    children = adjacency_list.get(node, [])

    if len(children) > 0:
        inorder_traversal(children[0], adjacency_list, visited)

    print(node, end=" ")

    for i in range(1, len(children)):
        inorder_traversal(children[i], adjacency_list, visited)


adj_list = {
    1: [2, 3],
    2: [5, 6],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

print_adjacency_matrix(adj_list)

try:
    start_node = int(input("\nEnter node : "))
    visited_nodes = [False] * (len(adj_list) + 1)
    print("InOrder Output:")
    inorder_traversal(start_node, adj_list, visited_nodes)
except ValueError:
    print("Invalid input! Please enter an integer.")