# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Using DFS
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], path: int) -> int:
        # Add node to path number
        path = path * 10 + root.val

        # Return if leaf
        if not (root.left or root.right):
            return path
        
        # If not, continue dfs
        result = 0
        if root.left:
            result += self.dfs(root.left, path)
        if root.right:
            result += self.dfs(root.right, path)
        return result
