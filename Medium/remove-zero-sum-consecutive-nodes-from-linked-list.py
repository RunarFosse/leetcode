# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using prefix sum
        prefix_sums = defaultdict(int)

        # To be able to remove first node, we initialize a "dummy node"
        start = ListNode(0, head)

        # Calculate prefix sum for all nodes,
        # storing last occurence in a dictionary
        current = start
        i, prefix = 0, 0
        while current:
            prefix += current.val
            prefix_sums[prefix] = i

            i, current = i+1, current.next
        
        # Then restart, skipping all nodes we can
        current = start
        i, prefix = 0, 0
        while current:
            prefix += current.val

            # Skip every node that together sum to 0
            next_node = current.next
            while next_node and i < prefix_sums[prefix]:
                i, next_node = i+1, next_node.next
            current.next = next_node

            i, current = i+1, current.next
        
        # Return the first node after dummy
        return start.next