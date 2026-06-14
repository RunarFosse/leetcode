# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Using two pointer

        # Iterate the linked list with a fast and slow pointer
        slow, fast, last = head, head, None
        while fast and fast.next:
            # Increment the fast pointer two steps
            fast = fast.next.next

            # Reverse the slow pointer's connection
            temp = slow.next
            slow.next = last
            last = slow
            slow = temp
        
        # Then, iterate each twin sum
        maximum = 0
        left, right = last, slow
        while left and right:
            # Storing the maximum twin sum
            maximum = max(left.val + right.val, maximum)

            left = left.next
            right = right.next
        
        # Finally, return this maximum twin sum
        return maximum
