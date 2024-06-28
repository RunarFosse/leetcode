# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Using greedy

        # First count occurence of each node
        degrees = [0] * n
        for edge in roads:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
        
        # Then sort each edge in ascending order, based on their degree
        nodes = sorted(range(n), key=lambda i : degrees[i])

        # Then calculate and sum over each importance of each node
        importance = 0
        for i, node in enumerate(nodes):
            importance += (i+1) * degrees[node]
        
        return importance
    
# We need to maximize the importance of all roads. This can be done
# by greedily assigning low importance to nodes with a smaller degree
# and high importance to nodes with a larger degree.
