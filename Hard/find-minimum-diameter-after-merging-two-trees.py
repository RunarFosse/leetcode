# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Using BFS

        # Compute the diameter of each tree separately
        diameter1 = self.computeDiameter(edges1)
        diameter2 = self.computeDiameter(edges2)

        # Then compute a diameter of them optimally merged
        combined = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Finally, return the maximum of all diameters
        return max(diameter1, diameter2, combined)
    
    def computeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        # First create an adjacency list
        adjls = defaultdict(list)
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)
        
        # Then find the furthest node in the graph
        queue, seen = deque([edges[0][0]]), set()
        while queue:
            node = queue.popleft()
            if node in seen:
                continue
            seen.add(node)

            queue += adjls[node]
        
        # Then find the node furthest away from this node
        queue, seen = deque([(node, 1)]), set()
        while queue:
            node, distance = queue.popleft()
            if node in seen:
                continue
            seen.add(node)

            # Store the diameter for later
            diameter = distance
            for neighbour in adjls[node]:
                queue.append((neighbour, distance + 1))
        
        # The diameter of the tree is the distance between these
        return diameter