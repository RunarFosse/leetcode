# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted, pointer = None, None
        
        queue = []
        for i, head in enumerate(lists):
            if head:
                queue.append((head.val, i))
        
        # Create built-in python priority queue!
        heapq.heapify(queue)

        while queue:
            _, i = heapq.heappop(queue)

            head = lists[i]
            if head.next:
                heapq.heappush(queue, (head.next.val, i))

            lists[i] = lists[i].next

            if not sorted:
                sorted = head
                pointer = sorted
            else:
                pointer.next = head
                pointer = pointer.next

        return sorted