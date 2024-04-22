# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Using BFS

        # First represent the graph as an adjacency list
        adjls = [[] for _ in range(n)]
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)

        # Then perform BFS from source to destination
        queue = deque([source])
        visited = set()
        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            # Check if already visited
            if node in visited:
                continue
            visited.add(node)
            
            # Add all neighbours to queue
            for neighbour in adjls[node]:
                queue.append(neighbour)
            
        # Return False if graph is searched without finding destination
        return False