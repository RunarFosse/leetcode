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
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft: bool = False) -> int:
        # Using DFS
        total = 0

        # Add sums from left
        if root.left:
            total += self.sumOfLeftLeaves(root.left, True)
        
        # And from right
        if root.right:
            total += self.sumOfLeftLeaves(root.right, False)
        
        # If is leaf, add if left
        if not (root.left or root.right) and isLeft:
            total += root.val
        
        return total