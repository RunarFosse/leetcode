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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Using DFS

        # Compute and return the sum of every number in the tree
        return self.dfs(root, 0)
    
    def dfs(self, node: Optional[TreeNode], path: int) -> List[int]:
        # If the node is null, it cannot have any number
        if not node:
            return 0

        # If not, add the current node's bit to the path
        path <<= 1
        path += node.val

        # If we are at a leaf node, return this path
        if not (node.left or node.right):
            return path
        
        # Otherwise, continue downwards, returning the sum of all numbers back upwards
        return self.dfs(node.left, path) + self.dfs(node.right, path)
