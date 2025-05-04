# Directed graph via adjacency‐list representation

class DirectedGraph:
    def __init__(self):
        # adjacency: { vertex: [outgoing_neighbors…], … }
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        """Add a directed edge u → v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)

    def __str__(self):
        lines = []
        for v in sorted(self.adj):
            nbrs = " ".join(self.adj[v])
            lines.append(f"{v} → {nbrs}")
        return "\n".join(lines)


if __name__ == "__main__":
    # build the graph from the assignment image:
    #   F → E,  E → G,  F → G,  G → H
    g = DirectedGraph()
    edges = [
        ("F", "E"),
        ("E", "G"),
        ("F", "G"),
        ("G", "H"),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    # print with your name label
    print("Edward's Graph (Adjacency list)")
    print(g)
