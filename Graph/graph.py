class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges.append((from_node, to_node))

    def print_graph(self):
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[1]}")

# Usage:
my_graph = Graph()
my_graph.add_node('A')
my_graph.add_node('B')
my_graph.add_node('c')
my_graph.add_node('D')
my_graph.add_node('E')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('C', 'D')
my_graph.add_edge('D', 'E')

my_graph.print_graph()
