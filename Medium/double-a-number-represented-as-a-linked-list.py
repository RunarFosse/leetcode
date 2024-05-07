# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using DFS

        # First unwrap whole linked list
        queue, current = [], head
        while current:
            queue.append(current)
            current = current.next
        
        # Then iterate from the back, doubling and adding carries
        carry = False
        while queue:
            node = queue.pop()

            # Double current
            node.val *= 2
            if carry:
                node.val += 1
                carry = False

            # If current is bigger than 1 digit, remove and add carry
            if node.val > 9:
                carry = True
                node.val -= 10
        
        # Check if there exists a residual carry, if so, create a new head
        if carry:
            head = ListNode(1, head)

        # Return the doubled list
        return head