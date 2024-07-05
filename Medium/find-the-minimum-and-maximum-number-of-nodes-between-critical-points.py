# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Keep track of last critical point, aswell as the first
        first_critical, last_critical = None, None

        # Keep track of the distances in a list
        distances = []

        # Iterate the list, updating distances 
        last, current = head, head.next
        index = 1
        while current.next:
            local_maxima = current.val > last.val and current.val > current.next.val
            local_minima = current.val < last.val and current.val < current.next.val
            if local_maxima or local_minima:
                # If we have not seen a critical point before
                if not first_critical:
                    # Count it
                    first_critical = index
                # However if we have
                else:
                    # Initialize distances list if needed
                    if not distances:
                        distances = [1e9, -1e9]

                    # Update distances
                    distances[0] = min(index - last_critical, distances[0])
                    distances[1] = index - first_critical

                # Update last critical as well
                last_critical = index

            # At last, continue iterating list
            last = current
            current = current.next
            index += 1
        
        # Finally, return [-1, -1] if distances list is uninitialized
        if not distances:
            return [-1, -1]
        
        # If not, return them
        return distances
