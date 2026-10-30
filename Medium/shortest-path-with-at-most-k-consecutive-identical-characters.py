# Author: Runar Fosse
# Time complexity: O((nk)log(nk))
# Space complexity: O(nk)

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Using Dijkstra's

        # First, create the graph
        adjls = [[] for _ in range(n)]
        for a, b, w in edges:
            adjls[a].append((b, w))
        
        # Then, find the shortest path using Dijkstra's
        queue, seen = [(0, 0, (labels[0], 1))], set()
        while queue:
            distance, node, (letter, count) = heappop(queue)

            # If we've seen more than k consecutive letters, or been here before
            if count > k or (node, letter, count) in seen:
                # Discard this path
                continue
            seen.add((node, letter, count))
            
            # If we've found the end
            if node == n - 1:
                # Return the shortest path
                return distance
            
            # Otherwise, traverse to neighbours
            for neighbour, weight in adjls[node]:
                new_letter = labels[neighbour]
                consecutive = (new_letter, (count + 1) if new_letter == letter else 1)
                heappush(queue, (distance + weight, neighbour, consecutive))
        
        # If loop terminates, there is no such path from 0 to n - 1
        return -1
