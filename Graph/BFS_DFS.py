def bfs(graph,start):
    visited=set()
    que=[start]
    while que:
        node=que.pop(0)
        if node not in visited:
            print(node,end='')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    que.append(neighbor)
visited=set()
  
def dfs(graph, node, visited):
    if node not in visited:
        print(node,end='')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
print("\nDFS OF GRAPH IS :")
dfs(graph,'A',visited)
