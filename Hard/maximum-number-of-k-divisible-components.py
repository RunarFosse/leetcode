# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Using topological sorting
        if not edges:
            return 1

        # First create the graph, keeping track of degree count
        adjls = defaultdict(list)
        degrees = defaultdict(int)
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        
        # Then start iterating from every leaf
        components = 0
        queue = deque([node for node in range(n) if degrees[node] == 1])
        while queue:
            node = queue.popleft()
            degrees[node] -= 1

            # If the value of the current subgraph is divisible by k, split
            if not values[node] % k:
                components += 1
            
            # Continue iterating neighbours
            for neighbour in adjls[node]:
                if not degrees[neighbour]:
                    continue

                # Remove current edge
                degrees[neighbour] -= 1

                # If this makes the neighbour a leaf, add to queue
                if degrees[neighbour] == 1:
                    queue.append(neighbour)

                # If we haven't split current subgraph, add value to neighbour
                if values[node] % k:
                    values[neighbour] += values[node]
        
        # Finally, return the number of components
        return components