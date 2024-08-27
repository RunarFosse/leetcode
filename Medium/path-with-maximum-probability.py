# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(m + n)

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Using Dijkstra's

        # Create an weighted graph
        adjls = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            adjls[a].append((b, prob))
            adjls[b].append((a, prob))
        
        # Perform Dijkstra's from start node (with max-heap)
        queue, seen = [(-1, start_node)], set()
        heapify(queue)
        while queue:
            distance, node = heappop(queue)
            if node in seen:
                continue
            seen.add(node)

            # If we've reached the end node, return the probability (distance)
            if node == end_node:
                return -distance

            # Add all neighbours to queue
            for neighbour, probability in adjls[node]:
                heappush(queue, (distance * probability, neighbour))
        
        # If while loop terminates, there is no path from start to end
        return 0