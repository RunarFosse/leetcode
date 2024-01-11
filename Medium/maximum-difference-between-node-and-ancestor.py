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
    def maxAncestorDiff(self, root: Optional[TreeNode], seen: Optional[Tuple[int]] = None) -> int:
        if not root:
            return 0

        # If seen doesn't exist, we are at the root
        if not seen:
            return max(self.maxAncestorDiff(root.left, (root.val, root.val)), self.maxAncestorDiff(root.right, (root.val, root.val)))
        
        # Calculate values for left and right subtrees
        new_seen = (min(seen[0], root.val), max(seen[1], root.val))
        left = self.maxAncestorDiff(root.left, new_seen)
        right = self.maxAncestorDiff(root.right, new_seen)

        # Calculate value for itself
        diff = max(abs(seen[0] - root.val), abs(seen[1] - root.val))

        # Return the maximum
        return max(diff, max(left, right))
        
# We can DFS the tree, storing the minimum and maximum intermediary value 
# we've seen, and returning the maximum possible difference between 
# this value and all other nodes in the same DFS path.