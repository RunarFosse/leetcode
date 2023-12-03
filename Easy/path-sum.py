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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Using DFS
        if not root:
            return False

        value = root.val 
        if value == targetSum and not (root.left or root.right):
            return True

        targetSum -= value
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)