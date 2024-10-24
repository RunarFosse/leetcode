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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Using DFS

        # Verify that roots are equal
        if not (root1 and root2):
            return not (root1 or root2)
        if root1.val != root2.val:
            return False
        
        # Check if subtrees are equivalent and not flipped
        if self.flipEquiv(root1.left, root2.left):
            return self.flipEquiv(root1.right, root2.right)
        
        # If not, check if flipped versions are equivalent
        if not self.flipEquiv(root1.left, root2.right):
            return False
        if not self.flipEquiv(root1.right, root2.left):
            return False

        return True