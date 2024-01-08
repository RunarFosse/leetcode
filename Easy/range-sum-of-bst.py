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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)

        # If current is within range, add to sum and iterate children
        if root.val >= low and root.val <= high:
            return root.val + left + right
        
        # If not, only iterate children
        return left + right