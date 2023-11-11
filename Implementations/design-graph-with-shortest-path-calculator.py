class Graph:
    # Add all edges to adjacency list
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjs = [[] for _ in range(n)]
        for node1, node2, w in edges:
            self.adjs[node1].append((node2, w))

    # Add new edge to adjacency list
    def addEdge(self, edge: List[int]) -> None:
        node1, node2, w = edge
        self.adjs[node1].append((node2, w))

    # Dijkstra to find shortest path
    def shortestPath(self, node1: int, node2: int) -> int:
        queue = []
        visited = set()
        heapify(queue)
        heappush(queue, (0, node1))
        while queue:
            dist, node = heappop(queue)
            if node == node2:
                return dist

            if node in visited:
                continue
            visited.add(node)
            
            for neighbour, w in self.adjs[node]:
                if neighbour not in visited:
                    heappush(queue, (dist+w, neighbour))
        
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)