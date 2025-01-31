# Author: Runar Fosse
# Time complexity: O(n(m + n))
# Space complexity: O(n)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Using Union-Find

        # Create a graph and Union-Find
        uf, self.adjls = UnionFind(n), [[] for _ in range(n)]
        for a, b in edges:
            self.adjls[a - 1].append(b - 1)
            self.adjls[b - 1].append(a - 1)
            uf.merge(a - 1, b - 1)

        # Then iterate every node
        max_groups = defaultdict(int)
        for node in range(n):
            # Use BFS to compute maximum number of groups from node
            groups = self.computeGroups(node)

            # If the current component cannot be grouped, return -1
            if groups == -1:
                return -1
            
            # If not, store current components maximum grouping
            component = uf.find(node)
            max_groups[component] = max(groups, max_groups[component])
        
        # Finally, return the sum of all maximum groups
        return sum(max_groups.values())
            
    def computeGroups(self, start: int) -> int:
        # Use BFS to compute maximum number of groups given start node
        max_groups = 0
        queue, groups = deque([(start, 1)]), {}
        while queue:
            node, distance = queue.popleft()
            if node in groups:
                continue
            groups[node] = distance
            
            # Remember current maximum groups
            max_groups = max(distance, max_groups)
            
            for neighbour in self.adjls[node]:
                # If we have seen a neighbour before
                if neighbour in groups:
                    # And they are not 1 group away
                    if groups[neighbour] != distance - 1:
                        # Then we cannot group the current component
                        return -1
                    continue
                queue.append((neighbour, distance + 1))

        # Return the final number of groups
        return max_groups

# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, size):
        self.root = []
        self.size = []
        for i in range(size):
            self.root.append(i)
            self.size.append(1)
    
    def find(self, node):
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]
        
# Optimally, we want to find the division leading to the maximum number
# of groups. If we assume that at least 1 group only has 1 node, we can
# start BFS from this node, and expand outwards, computing number of groups.
# In this way, we can find the maximum number of groups for each disconnected
# component. 
# Using Union-Find we can easily divide and identify disjoint sets.