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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # If root is a leaf
        if not (root.left or root.right):
            return 1
        
        # If not, find minimum depth of children
        minDepth = 1e9
        if root.right:
            minDepth = min(self.minDepth(root.right), minDepth)
        if root.left:
            minDepth = min(self.minDepth(root.left), minDepth)
        
        return 1 + minDepth