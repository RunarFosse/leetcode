# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Using DFS
        n = len(edges)
        
        # First, DFS from node1 and node2, storing respective distances for each
        distances1 = self.dfs(node1, edges)
        distances2 = self.dfs(node2, edges)
        
        # Then, iterate each node
        node, distance = -1, 1e9
        for i in range(n):
            # If a node is reachable by both node1 and node2
            if i in distances1 and i in distances2:
                # Store it if it minimizes maximum distance from both
                current = max(distances1[i], distances2[i])
                if current < distance:
                    node, distance = i, current
        
        # Finally, return the node with this smallest distance
        return node

    def dfs(self, node: int, edges: List[int]) -> Dict[int, int]:
        distance, distances = 0, {}
        while node != -1 and node not in distances:
            distances[node] = distance
            node = edges[node]
            distance += 1

        return distances
        