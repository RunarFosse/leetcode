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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right

        # Calculate the diameter of current node
        currentDiameter = self.maxHeight(left) + self.maxHeight(right)
        leftDiameter = self.diameterOfBinaryTree(left)
        rightDiameter = self.diameterOfBinaryTree(right)

        # Compare it and return the max in the whole subtree
        return max(currentDiameter, leftDiameter, rightDiameter)

    @functools.cache
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Calculate the max height in subtree and return it
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        return max(leftHeight, rightHeight) + 1