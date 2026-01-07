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
    mod = int(1e9 + 7)
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Using BFS

        # Compute the subtree sum of every subtree using BFS
        subtrees = []
        total = self.bfs(root, subtrees)

        # Then, find the maximum product when splitting on each subtree
        maximum = max(subtree * (total - subtree) for subtree in subtrees)

        # And return it modulo
        return maximum % self.mod
    
    def bfs(self, node: Optional[TreeNode], subtrees: List[int]) -> int:
        # Compute the sum of the current subtree
        if not node:
            return 0
        
        # By computing it on both sides, and adding the current value
        left = self.bfs(node.left, subtrees)
        right = self.bfs(node.right, subtrees)
        current = node.val + left + right
        
        # Adding it to the subtree sum array, and returning it upwards
        subtrees.append(current)
        return current
