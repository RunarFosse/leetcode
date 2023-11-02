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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # Using DFS
        _, _, averages = self.dfs(root)
        return averages
        
    def dfs(self, root: TreeNode) -> (int, int, int):
        values, nodes, averages = root.val, 1, 0

        if root.left:
            left_val, left_nodes, left_avg = self.dfs(root.left)
            values += left_val
            nodes += left_nodes
            averages += left_avg
        
        if root.right:
            right_val, right_nodes, right_avg = self.dfs(root.right)
            values += right_val
            nodes += right_nodes
            averages += right_avg
        
        mean = values // nodes
        if mean == root.val:
            averages += 1
        
        return values, nodes, averages
        