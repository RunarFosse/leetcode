# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Using DFS

        # First, create the graph
        adjls = defaultdict(list)
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)

        # Compute the maximum depth of the tree
        maximum, queue = 0, [(1, 0, -1)]
        while queue:
            node, depth, parent = queue.pop()
            maximum = max(depth, maximum)
            
            for neighbour in adjls[node]:
                if neighbour != parent:
                    queue.append((neighbour, depth + 1, node))
        
        # Compute the number of ways to assign weights resulting in a odd total cost
        ways = pow(2, maximum - 1, self.mod)

        # And return it
        return ways


# Given the a node of maximum depth x. Then the path from 1 to that will have x edges.
# To ensure that the path has an odd cost we need to keep the weight of one edge fixed.
# The reason is this, either:
# 1. The other x - 1 edges have an odd total cost
# 2. The other x - 1 edges have a even total cost

# For 1. the final edge weight needs to be 2, for 2. it has to be 1

# This gives us 2^(x - 1) possible combinations in total for a path of maximum depth x.