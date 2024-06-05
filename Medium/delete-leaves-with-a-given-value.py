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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Using DFS
        if not root:
            return None

        # DFS down until we've reached a leaf node
        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)

        # Override current node due to updated children in DFS
        root.left, root.right = left, right

        # Finally, return upwards 
        if not (root.left or root.right):
            return None if root.val == target else root
        return root
        