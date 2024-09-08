# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # First find the length of the linked list
        length, current = 0, head
        while current:
            current = current.next
            length += 1
        
        # Then calculate the length of each list, as well as remainder
        sublength, remainder = divmod(length, k)
        
        # Finally split the list into k parts
        parts = []
        for _ in range(k):
            # If head is None, there are no more listnodes to add
            if not head:
                parts.append(None)
                continue
            
            # However if not, add head and iterate until part is filled
            parts.append(head)
            for _ in range(sublength - 1 + (1 if remainder else 0)):
                head = head.next
            
            # Decrement remainder if we've added an additional node
            if remainder:
                remainder -= 1
            
            # Finally, if the list contains more nodes, disjoin this part
            if head:
                head.next, head = None, head.next
        
        # Return the linked list in parts
        return parts
        