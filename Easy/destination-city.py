# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Add to adjacency
        adjacency = {}
        for a, b in paths:
            adjacency[a] = b
        
        # Iterate path
        current = paths[0][0]
        while next := adjacency.get(current):
            current = next
        return current

# Add all path to adjacency dictionary. Then iterate path until end is reached