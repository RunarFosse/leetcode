# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n+m)

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Using topological sorting

        # First create adjacency list and count the indegree of each node
        indegrees = [0] * n
        adjls = [[] for _ in range(n)]
        for a, b in edges:
            indegrees[b] += 1
            adjls[a].append(b)
            adjls[b].append(a)

        # Then via topological sort, traverse nodes where all ancestors
        # have already been visited, and calculate list of ancestors
        ancestors = [set() for _ in range(n)]
        queue = deque([node for node in range(n) if not indegrees[node]])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            
            for neighbour in adjls[node]:
                if neighbour in visited:
                    # Add neighbour and its ancestors to current's
                    ancestors[node].add(neighbour)
                    ancestors[node].update(ancestors[neighbour])
                    continue

                indegrees[neighbour] -= 1
                if not indegrees[neighbour]:
                    queue.append(neighbour)
        
        # Return list of ancestors for each node
        return list(map(lambda s: sorted(list(s)), ancestors))
            