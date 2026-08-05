# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Using BFS

        # First, create the graph
        adjls = [[] for _ in range(n)]
        for a, b in invocations:
            adjls[a].append(b)
        
        # Then, mark every method called by k suspicious
        queue, suspicious = deque([k]), [False] * n
        while queue:
            node = queue.popleft()
            if suspicious[node]:
                continue
            suspicious[node] = True

            for invoked in adjls[node]:
                queue.append(invoked)
        
        # Again, iterate every method invokation
        for a, b in invocations:
            # If we ever have a non-suspicious method calling a supicious one
            if not suspicious[a] and suspicious[b]:
                # Then no node in the graph is suspicious
                suspicious = [False] * n
                break

        # At last, return every non-supicious node
        return [i for i in range(n) if not suspicious[i]]
