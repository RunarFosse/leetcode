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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using DFS
        _, subtree = self.dfs(root)
        return subtree
    
    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
        if node is None:
            return (0, None)
        
        # Traverse down left and right sides
        ldepth, lsubtree = self.dfs(node.left)
        rdepth, rsubtree = self.dfs(node.right)

        # Check their depths, and return the deepest
        if ldepth > rdepth:
            depth, subtree = ldepth, lsubtree
        elif ldepth < rdepth:
            depth, subtree = rdepth, rsubtree
        else:
            # However, if they are equally deep, return this node
            depth, subtree = ldepth, node
        
        # And increment depth counter
        return depth + 1, subtree
