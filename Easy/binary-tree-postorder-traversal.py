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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Using DFS
        traversal = []
        self.dfs(root, traversal)
        return traversal
    
    def dfs(self, root: Optional[TreeNode], traversal: List[int]) -> None:
        if not root:
            return
        
        # First traverse children
        self.dfs(root.left, traversal)
        self.dfs(root.right, traversal)
        
        # Then add current visited node to traversal array
        traversal.append(root.val)