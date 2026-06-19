# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(nlog n)

class Solution:
    mod = int(1e9 + 7)
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Using LCA
        n = len(edges) + 1

        # First, create the graph
        adjls = [[] for _ in range(n + 1)]
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)

        # Compute the number of binary-lifting columns needed to jump up to n
        self.columns = n.bit_length()

        # And store a binary-lifting ancestor table of the nodes, plus their depth
        self.ancestors = [[-1] * self.columns for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        # Then, DFS the tree
        queue = [(1, 0, -1)]
        while queue:
            node, depth, parent = queue.pop()
            self.depth[node] = depth

            for neighbour in adjls[node]:
                if neighbour != parent:
                    queue.append((neighbour, depth + 1, node))

            # Add parents to the binary-lifting ancestor table
            self.ancestors[node][0] = parent
            for distance in range(1, self.columns):
                middle = self.ancestors[node][distance - 1]
                if middle == -1:
                    self.ancestors[node][distance] = -1
                else:
                    self.ancestors[node][distance] = self.ancestors[middle][distance - 1]

        # Finally, iterate each of the queries
        answer = []
        for a, b in queries:
            # If they are the same node, the answer is always 0
            if a == b:
                answer.append(0)
                continue
            
            # Otherwise, compute the length of the path between the two nodes
            lca = self.computeLCA(a, b)
            length = self.depth[a] + self.depth[b] - 2 * self.depth[lca]
        
            # Compute the answer as the number of ways to get an odd total cost
            answer.append(pow(2, length - 1, self.mod))

        # Return the answer to all the queries
        return answer

    def computeLCA(self, a: int, b: int) -> int:
        # Compute the lowest common ancestor of both nodes
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        
        # Move the deepest node up to the same level as the other
        for column in reversed(range(self.columns)):
            if self.depth[a] - (1 << column) >= self.depth[b]:
                a = self.ancestors[a][column]
        
        # If they are the same node, we have found our LCA
        if a == b:
            return a
        
        # Otherwise, move both up until they have the same closest parent
        for column in reversed(range(self.columns)):
            if self.ancestors[a][column] != self.ancestors[b][column]:
                a = self.ancestors[a][column]
                b = self.ancestors[b][column]
        
        # And return it, as that parent is the LCA
        return self.ancestors[a][0]


# Follows the same argumentation as https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i.