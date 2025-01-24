# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Using topological sorting
        n = len(graph)
        
        # Iterate the graph, storing innodes and outdegree per node
        innodes, outdegree = [[] for _ in range(n)], [0] * n
        for node in range(n):
            neighbours = graph[node]
            outdegree[node] = len(neighbours)
            for neighbour in neighbours:
                innodes[neighbour].append(node)
        
        # Store initial safe nodes in a queue, and iterate
        queue = [node for node in range(n) if not outdegree[node]]
        safe = [False] * n
        while queue:
            node = queue.pop()

            # Mark the node as safe
            safe[node] = True

            # Remove node from innode neighbours
            for innode in innodes[node]:
                # By decrementing its outdegree
                outdegree[innode] -= 1

                # If it becomes zero, add to queue
                if not outdegree[innode]:
                    queue.append(innode)
        
        # At last, return all safe nodes in ascending order
        return [node for node in range(n) if safe[node]]
