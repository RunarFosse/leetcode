# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        # Count indegrees for each node
        indegree = [0] * n
        for _, b in edges:
            indegree[b] += 1
        
        # Champions are every node with indegree 0
        champions = [i for i in range(n) if not indegree[i]]
        return champions[0] if len(champions) == 1 else -1