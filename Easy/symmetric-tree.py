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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Using preorder/postorder traversal

        # Base cases
        if not root:
            return True
        if not (root.left and root.right):
          return not (root.left or root.right)
        
        # Preorder left, postorder right
        lqueue, rqueue = deque([root.left]), deque([root.right])
        while lqueue and rqueue:
            # Left subtree
            left = lqueue.popleft()
            # Right subtree
            right = rqueue.popleft()

            # If only one side exists, the tree can't be symmetric
            if (left or right) and not (left and right):
              return False
            # If neither exist, we continue (tree might still be symmetric)
            if not (left and right):
              continue

            # Verify that both sides are equal
            if not (left.val == right.val):
              return False
            
            # Add left subtree in preorder
            lqueue.appendleft(left.right)
            lqueue.appendleft(left.left)
            # Add right subtree in postorder
            rqueue.appendleft(right.left)
            rqueue.appendleft(right.right)
        
        # Verify that both subtrees are empty
        return not (lqueue or rqueue)
    
# Perform preorder-traversal on left subtree, postorder- on right subtree.
# Continuously compare.