# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(m + n)

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Using Dijkstra's

        # First, create the graph
        adjls = [[] for _ in range(n)]
        for a, b, weight in edges:
            adjls[a].append((b, weight))

            # Also add switch possibility
            adjls[b].append((a, 2 * weight))
        
        # Then, traverse the graph
        queue, seen = [(0, 0)], set()
        while queue:
            distance, node = heappop(queue)

            # If we've seen the node before, skip it
            if node in seen:
                continue
            seen.add(node)

            # If we've reached the end, return the distance
            if node == n - 1:
                return distance

            # Traverse to all neighbouring nodes, including switched ones
            for neighbour, weight in adjls[node]:
                heappush(queue, (distance + weight, neighbour))
        
        # If loop terminates, it is not possible to reach the end node
        return -1
