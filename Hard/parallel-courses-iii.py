# Author: Runar Fosse
# Time complexity: O(n + m)
# Space complexity: O(n + m)

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegrees = [0] * n
        children = [[] for _ in range(n)]
        # Store indegrees, children, and at the same time make
        # courses 0-indexed (0 to n-1)
        for node, child in relations:
            indegrees[child-1] += 1
            children[node-1].append(child-1)

        # Node with no parents are sources
        queue = []
        timetocomplete = [0] * n
        for i in range(n):
            if not indegrees[i]:
                queue.append(i)
                timetocomplete[i] = time[i]
        
        while queue:
            i = queue.pop(0)
            
            for child in children[i]:
                timetocomplete[child] = max(timetocomplete[i] + time[child], timetocomplete[child])
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        return max(timetocomplete)
        
        
# Turn problem into (possibly several) acyclic graphs.
# Store all different source nodes in graph, and find path through graph.
# Solution is path through a graph taking maximal time. \/

# Sequentially find time to solve earlier nodes, concluding in calculation
# of all paths through every graph. The solution is the max time for a given
# node to be complete.