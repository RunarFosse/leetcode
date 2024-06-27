# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Extract the first two edges
        (a, b), (c, d) = edges[0], edges[1]

        # Return the node which appear in both
        return a if (a == c or a == d) else b
        

# In this star graph, every node can be either an edge or the center.
# An edge only has one outgoing edge, where the center has n-1.
# Therefore, we only need to check two edges, to find the node connected to
# both. This will be the center node of the start graph!