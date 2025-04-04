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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using DFS
        return self.dfs(root)[0]
    
    def dfs(self, root: Optional[TreeNode]) -> (Optional[TreeNode], int):
        if not root:
            return (None, -1)
        
        # Get depth of children
        left, right = self.dfs(root.left), self.dfs(root.right)

        # If they are equal, replace with LCA
        if left[1] == right[1]:
            return (root, left[1] + 1)
        
        # Otherwise, return deepest
        if left[1] > right[1]:
            return (left[0], left[1] + 1)
        else:
            return (right[0], right[1] + 1)