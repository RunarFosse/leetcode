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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.pathsHelper(root, "")
    
    def pathsHelper(self, root: Optional[TreeNode], prefix: str) -> List[str]:
        if not root:
            return []

        # Is a leaf node
        if not (root.left or root.right):
            return [ prefix + str(root.val) ]
        
        new_prefix = prefix + str(root.val) + "->"
        return self.pathsHelper(root.left, new_prefix) + self.pathsHelper(root.right, new_prefix)