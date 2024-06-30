# Author: Runar Fosse
# Time complexity: O(mlog m)
# Space complexity: O(n+m)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Using Union Find

        # First sort edges such that type 3 appear first
        edges.sort(key = lambda edge: edge[0], reverse=True)

        # Create a Union Find for both Alice and Bob
        alice = UnionFind(n)
        bob = UnionFind(n)

        # For each edge, check if it should be added to graph
        # by checking if the addition of the edge makes a cycle
        # in both (!) trees
        edge_count = 0
        for edge in edges:
            should_add = False
            if edge[0] in {1, 3}:
                should_add |= alice.union(edge[1]-1, edge[2]-1)
            if edge[0] in {2, 3}:
                should_add |= bob.union(edge[1]-1, edge[2]-1)
            
            # Add the edge to the new graph if any person 
            # which can traverse it needs it
            if should_add:
                edge_count += 1
        
        # If any person cannot traverse the whole graph, return -1
        if not (alice.is_connected() and bob.is_connected()):
            return -1
        
        # Return the number of edges removed from first graph
        return len(edges) - edge_count


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
    
    def find(self, node: int) -> int:
        # Find parent of node
        while self.parent[node] != node:
            temp = self.parent[node]
            # Optimize later finds using Path Compression
            self.parent[node] = self.parent[temp]
            node = temp
        return node
    
    def union(self, node1: int, node2: int) -> bool:
        # Find parent of each node
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        # If they share a parent node, don't add edge
        if parent1 == parent2:
            return False
        
        # If not, add edge by setting parent of one to be the other
        self.parent[parent2] = parent1
        return True
    
    def is_connected(self) -> bool:
        # The graph is connected if all nodes have the same parent
        return all(self.find(i) == self.parent[0] for i in range(self.n))

# This problem asks us to remove edges such that the joint graph is 
# a minimum spanning tree for both Alice and Bob.

# This can be done through e.g. Kruskal's algorithm (but not
# adding edges which make the graph a cycle), prioritizing
# adding type 3 edges first, as these benefit both people.