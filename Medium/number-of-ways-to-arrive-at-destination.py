# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(m + n)

class Solution:
    mod = int(1e9 + 7)
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Using Dijkstra's

        # First, build the graph
        adjls = [[] for _ in range(n)]
        for a, b, weight in roads:
            adjls[a].append((b, weight))
            adjls[b].append((a, weight))
        
        # Then, traverse the graph using Dijkstra's algorithm
        queue = [(0, 0)]
        distances, ways = [0] + [inf] * (n - 1), [1] + [0] * (n - 1)
        while queue:
            distance, node = heappop(queue)
            if distance > distances[node]:
                continue
            
            # Iterate all neighbour nodes
            for neighbour, weight in adjls[node]:
                # Compute the new distance to the node
                new_distance = distance + weight

                # If we've been there before with the same distance
                if new_distance == distances[neighbour]:
                    # Increment the number of ways we can get to this neighbour
                    ways[neighbour] += ways[node]
                    ways[neighbour] %= self.mod

                # Otherwise, if this is the current shortest path to our neighbour
                if new_distance < distances[neighbour]:
                    # Update distance, ways and add it to the queue
                    distances[neighbour] = new_distance
                    ways[neighbour] = ways[node]
                    heappush(queue, (new_distance, neighbour))
        
        # Finally, return the number of ways to reach the destination at the shortest time
        return ways[n - 1]
