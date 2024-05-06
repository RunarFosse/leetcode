# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Shift every value to the right one to the left
        last = None
        while node.next:
            node.val = node.next.val
            last, node = node, node.next

        # And remove last node from list
        last.next = None
        