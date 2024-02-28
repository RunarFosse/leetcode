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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Using BFS

        # Perform BFS to last level
        queue = deque([root])
        while queue:
            node = queue.popleft()

            # Add right and left, in that order, if they exist
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        # The leftmost value of the last row will now be node
        return node.val
        
