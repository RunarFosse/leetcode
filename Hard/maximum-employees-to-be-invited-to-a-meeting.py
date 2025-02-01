# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Using topological sorting
        n = len(favorite)

        # First count indegrees
        indegree = [0] * n
        for employee in favorite:
            indegree[employee] += 1

        # Store depth of all nodes, when they are part of a non-cycle
        depth = [1] * n
        
        # Perform topological sort to remove non-cyclic nodes
        queue = deque([i for i in range(n) if not indegree[i]])
        while queue:
            employee = queue.popleft()

            # Increment the depth of favorite
            depth[favorite[employee]] = max(depth[employee] + 1, depth[favorite[employee]])
            
            # Remove employee from indegree of favorite, and add to queue if 0
            indegree[favorite[employee]] -= 1
            if not indegree[favorite[employee]]:
                queue.append(favorite[employee])
        
        # Then, compute the largest cycle, or a size of the table of chains
        max_cycle, chains = 0, 0
        for employee in range(n):
            # If indegree is 0, we have already computed their cycle
            if not indegree[employee]:
                continue
            
            # Otherwise, DFS cycle size
            node, cycle = employee, 0
            while indegree[node]:
                # Increment cycle size, mark node as visited and continue
                cycle += 1
                indegree[node] = 0
                node = favorite[node]
            
            # If we have a cycle of size 2, we can add the largest amount 
            # of non-cyclic neighbours to the table (i.e. the chain)
            if cycle == 2:
                chains += depth[employee] + depth[favorite[employee]]
            else:
                max_cycle = max(cycle, max_cycle)

        # At last, return the maximum cycle or chain
        return max(max_cycle, chains)