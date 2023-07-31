
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def dfs(graph, start):
    visited = set()

    def dfs_util(node):
        visited.add(node)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_util(neighbor)

    dfs_util(start)


# Example Usage:

# Create a graph represented using an adjacency list
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Perform BFS starting from node 2
print("BFS Traversal:")
bfs(graph, 2)
print()

# Perform DFS starting from node 2
print("DFS Traversal:")
dfs(graph, 2)
