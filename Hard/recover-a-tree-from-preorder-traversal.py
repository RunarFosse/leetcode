# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Using DFS
        self.n, self.traversal = len(traversal), traversal
        return self.dfs(0, 0)[0]
    
    def dfs(self, i: int, depth: int) -> Tuple[TreeNode, int, int]:
        # First, get the current node and its value
        node = TreeNode()
        while i < self.n and self.traversal[i].isnumeric():
            node.val *= 10
            node.val += int(self.traversal[i])
            i += 1

        # Then, compute the depth of the next node
        next_depth = 0
        while i < self.n and self.traversal[i] == "-":
            next_depth += 1
            i += 1
        
        # If the next depth is equal to or smaller than this one
        if next_depth <= depth:
            # Return this current node upwards
            return (node, next_depth, i)

        # Otherwise, continue downwards
        node.left, next_depth, i = self.dfs(i, next_depth)

        # Again, based on depth either return upwards
        if next_depth <= depth:
            return (node, next_depth, i)
        
        # Or retrieve next node
        node.right, next_depth, i = self.dfs(i, next_depth)

        # Finally, return node upwards
        return (node, next_depth, i)
