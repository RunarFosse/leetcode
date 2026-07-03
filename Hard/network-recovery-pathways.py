# Author: Runar Fosse
# Time complexity: O((m + n)log w)
# Space complexity: O(m + n)

# where w is the maximum edge weight

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # Using binary search
        self.n, self.k = len(online), k

        # First, create the graph
        left, right = 1e9, 0
        adjls, indegrees = [[] for _ in range(self.n)], [0] * self.n
        for a, b, weight in edges:
            # If either node is offline, skip the edge
            if not(online[a] and online[b]):
                continue
            adjls[a].append((b, weight))
            indegrees[b] += 1

            # And store binary search bounds
            left = min(weight, left)
            right = max(weight, right)
        
        # Then, remove all unreachable online nodes
        queue = deque([node for node in range(1, self.n) if not indegrees[node]])
        while queue:
            node = queue.popleft()
            for neighbour, _ in adjls[node]:
                indegrees[neighbour] -= 1
                if neighbour and not indegrees[neighbour]:
                    queue.append(neighbour)
        
        # If there are no valid paths even with no edge weight minimum
        if not self.validPath(adjls, indegrees.copy(), 0):
            # Then there are no valid paths at all
            return -1
        
        # Otherwise, binary search the maximum path score
        while left <= right:
            pivot = (left + right) // 2

            # Depending on wether we have a valid path, update bounds
            if self.validPath(adjls, indegrees.copy(), pivot):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # Finally, return this maximum path score
        return left - 1

    def validPath(self, adjls: List[List[Tuple[int, int]]], indegrees: List[int], minimum_weight: int) -> bool:
        # Using topological sort, traverse the graph
        queue, costs = deque([0]), [0] + [inf] * (self.n - 1)
        while queue:
            node = queue.popleft()
            
            # If we reach the end
            if node == self.n - 1:
                # We might have a valid path, depending on the cost
                return costs[node] <= self.k
            
            # Iterate all the neighbours
            for neighbour, weight in adjls[node]:
                # Only update costs of node with we actually can traverse the edge
                if weight >= minimum_weight:
                    costs[neighbour] = min(costs[node] + weight, costs[neighbour])
                indegrees[neighbour] -= 1
                # And add to queue if next in line topologically
                if not indegrees[neighbour]:
                    queue.append(neighbour)
        
        # If loop terminates, we do not have a valid path
        return False
