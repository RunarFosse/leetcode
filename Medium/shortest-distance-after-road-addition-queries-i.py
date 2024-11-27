# Author: Runar Fosse
# Time complexity: O(m(n + m))
# Space complexity: O(n + m)

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Using BFS

        # First create the graph
        adjls = [[i+1] if i < n - 1 else [] for i in range(n)]

        # Then for each query, compute minimum distance
        distances = []
        for a, b in queries:
            # Add edge to graph
            adjls[a].append(b)

            # And BFS distance
            queue, seen = deque([(0, 0)]), set()
            while queue:
                node, distance = queue.popleft()
                if node == n-1:
                    distances.append(distance)
                    break

                if node in seen:
                    continue
                seen.add(node)

                for neighbour in adjls[node]:
                    queue.append((neighbour, distance + 1))
        
        # Finally, return all distances
        return distances