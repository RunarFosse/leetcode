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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        # Left side needs to be added, unless both are empty
        left, right = "", ""
        if root.left or root.right:
            left = "(" + self.tree2str(root.left) + ")"
        if root.right:
            right = "(" + self.tree2str(root.right) + ")"

        return str(root.val) + left + right
