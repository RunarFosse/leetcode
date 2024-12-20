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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using DFS
        self.dfs(root.left, root.right, True)
        return root
    
    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode], odd: bool):
        # If we are at the end of the tree, return
        if not (left or right):
            return
        
        # If we are at a odd level, reverse levels
        if odd:
            left.val, right.val = right.val, left.val
        
        # And continue recursing
        self.dfs(left.left, right.right, not odd)
        self.dfs(left.right, right.left, not odd)
        

        