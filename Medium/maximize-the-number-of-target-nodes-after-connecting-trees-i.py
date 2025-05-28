# Author: Runar Fosse
# Time complexity: O(m^2 + n^2)
# Space complexity: O(m + n)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Using BFS
        n, m = len(edges1), len(edges2)

        # First, create both graphs
        adjls1 = defaultdict(list)
        for a, b in edges1:
            adjls1[a].append(b)
            adjls1[b].append(a)
        adjls2 = defaultdict(list)
        for u, v in edges2:
            adjls2[u].append(v)
            adjls2[v].append(u)

        # First, find the maximum number of
        # targets a node has in graph2, for k - 1
        targets2 = max(self.bfs(i, k - 1, adjls2) for i in range(m + 1))
        
        # Then, for each node in graph1, find the number of targets
        # if it has an edge to the node in graph1 with the most targets
        targets1 = [targets2 + self.bfs(i, k, adjls1) for i in range(n + 1)]

        # Finally, return the maximum number of targets for each node in graph1
        return targets1
    
    def bfs(self, i: int, k: int, adjls: List[int]) -> int:
        # Count number of targets for a given k
        targets = 0
        queue, seen = deque([(i, 0)]), set()
        while queue:
            node, distance = queue.popleft()
            if node in seen:
                continue
            seen.add(node)

            # If we ever reach a distance more than k, break
            if distance > k:
                break
            targets += 1

            for neighbour in adjls[node]:
                queue.append((neighbour, distance + 1))
        
        return targets
            