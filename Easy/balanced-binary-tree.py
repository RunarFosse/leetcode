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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balancedDepth(root) >= 0
    
    def balancedDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self.balancedDepth(root.left)
        depth_right = self.balancedDepth(root.right)

        if abs(depth_left - depth_right) > 1:
            return -1e9
        
        return 1 + max(depth_left, depth_right)