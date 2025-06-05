# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Using Union-Find

        # First, combine all equivalent characters in a Union-Find
        uf = UnionFind()
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)
        
        # Then, compute and return the smallest equivalent string
        return "".join([uf.find(c) for c in baseStr])


class UnionFind:
    def __init__(self):
        self.parent = {c: c for c in "abcdefghijklmnopqrstuvwxyz"}
    
    def find(self, node: str) -> str:
        # Find parent of node
        while self.parent[node] != node:
            temp = self.parent[node]
            # Optimize later finds using Path Compression
            self.parent[node] = self.parent[temp]
            node = temp
        return node
    
    def union(self, node1: str, node2: str):
        # Find parent of each node
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        # And connect them, by setting the lexicographically smallest as the parent
        if parent1 < parent2:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2