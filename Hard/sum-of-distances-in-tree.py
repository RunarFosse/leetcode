# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Using DFS
        self.sums = [0] * n
        self.counts = [0] * n

        # First create adjacency list
        self.adjls = [[] for _ in range(n)]
        for a, b in edges:
            self.adjls[a].append(b)
            self.adjls[b].append(a)

        # Then initialize by calculating DFS from node 0 
        self.sums[0], _ = self.initial_dfs(0, None)
    
        # Then use the formula to calculate rest through dfs
        queue = [(0, None)]
        visited = set()
        while queue:
            node, last = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            
            # Formula only works given a parent node
            if last != None:
                self.sums[node] = self.sums[last] + n - 2*self.counts[node]
            
            # Append all deeper neighbour nodes
            for neighbour in self.adjls[node]:
                if neighbour == last:
                    continue
                queue.append((neighbour, node))

        # Return all sums
        return self.sums

    def initial_dfs(self, root: int, last: int) -> (int, int):
        sums, count = 0, 1
        
        # Search down all neighbours
        for neighbour in self.adjls[root]:
            if neighbour == last:
                continue
            sub_sums, sub_count = self.initial_dfs(neighbour, root)

            # Add subtree sum and counts to current
            sums += sub_sums + sub_count
            count += sub_count
        
        # Store count in global list
        self.counts[root] = count

        return sums, count
    
    
# Given that we have the sum of all distances for a single arbitrary node, we
# can easily calculate the sum of all distances from another neighbour node:
#
# sums(i) = sums(j) - counts(i) + n - counts(i) = sum(j) + n - 2 * counts(i)
#
# where counts(i) - number of nodes in the subtree rerooted in node i
#
# counts(i) can easily be calculated with one pass of DFS from arbitrary
# full root of tree in node 0.