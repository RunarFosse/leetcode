# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Using DFS
        if not root:
            return False

        # If the root creates the downward linked list path, return True
        if self.createsPath(root, head):
            return True
            
        # If not, check if children do
        left = self.isSubPath(head, root.left)
        right = self.isSubPath(head, root.right)
        return left or right
    
    def createsPath(self, root: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        # Using DFS
        if not head:
            return True
        if not root or root.val != head.val:
            return False
        
        left = self.createsPath(root.left, head.next)
        right = self.createsPath(root.right, head.next)
        return left or right