# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # Using DFS
        n = len(parent)

        # Flip the graph
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)
        
        # Then, perform DFS, updating tree and computing subtree sizes
        subtrees, ancestors = [1] * n, [None] * 26
        self.s, self.indexOf = s, lambda c: ord(c) - ord("a")
        self.dfs(0, -1, subtrees, ancestors)

        # And return these updated tree's subtree sizes
        return subtrees

    def dfs(self, node: int, parent: int, subtrees: List[int], ancestors: List[int]) -> None:
        # If this node has an ancestor of the same character
        index = self.indexOf(self.s[node])
        ancestor = ancestors[index]
        if ancestor is not None:
            # Set that as our current parent
            parent = ancestor

        # Temporarily update the ancestor table
        ancestors[index] = node
        
        # Iterate the tree downwards
        for child in self.children[node]:
            self.dfs(child, node, subtrees, ancestors)
        
        # Then revert the prior ancestor update
        ancestors[index] = ancestor

        # And update the parent's subtree size after updating subtree
        if node > 0:
            subtrees[parent] += subtrees[node]
