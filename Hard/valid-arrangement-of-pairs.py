# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # First create a graph, and count indegrees
        adjls = defaultdict(list)
        indegree, outdegree = defaultdict(int), defaultdict(int)
        for a, b in pairs:
            adjls[a].append(b)

            outdegree[a] += 1
            indegree[b] += 1
        
        # To start the arrangement, find the node with a higher outdegree
        # than indegree, as this denotes a source
        start = pairs[0][0]
        for node in adjls:
            if indegree[node] < outdegree[node]:
                start = node
        
        # Store the current path on a stack
        stack = [start]
        path = []

        # While there is a node on the stack
        while stack:
            # Iterate a path until its end
            while adjls[stack[-1]]:
                stack.append(adjls[stack[-1]].pop())

            # And append the last node to the path
            path.append(stack.pop())

        # Finally, create the arrangement, by iterating path in reverse order
        return [[path[i + 1], path[i]] for i in range(len(path)-2, -1, -1)]