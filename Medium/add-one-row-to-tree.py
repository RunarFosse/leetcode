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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, left: bool = True) -> Optional[TreeNode]:
        # Using DFS

        # If depth is 1, then we should add row
        if depth == 1:
            subtree = TreeNode(val)
            if left:
                subtree.left = root
            else:
                subtree.right = root
            
            # Return back up
            return subtree
        
        # If not, propogate function downwards (if current node exists)
        if root:
            root.left = self.addOneRow(root.left, val, depth-1, True)
            root.right = self.addOneRow(root.right, val, depth-1, False)
        return root