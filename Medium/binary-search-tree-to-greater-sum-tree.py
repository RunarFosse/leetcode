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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Using DFS
        self.seen = 0
        return self.dfs(root)
    
    def dfs(self, root: TreeNode) -> TreeNode:
        # Reverse in-order traversal
        if (root.right):
            root.right = self.dfs(root.right)

        # Add current to seen and re-set value
        self.seen += root.val
        root.val = self.seen

        if (root.left):
            root.left = self.dfs(root.left)
        
        # Return modified subtree
        return root

# This problem is simply solved using reversed (starting from right node)
# in-order traversal and keeping a global sum of seen values, and adding
# this to new visited nodes.