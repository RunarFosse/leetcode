# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # First we create the matrix, initialized with -1
        matrix = [[-1] * n for _ in range(m)]

        # Then traverse the linked list
        position, direction = [0, 0], [0, 1]
        while head:
            # Fill the current position with node
            matrix[position[0]][position[1]] = head.val

            # And move forward
            position[0] += direction[0]
            position[1] += direction[1]
            head = head.next

            # If we reach a corner, go back and turn 90 degrees right
            yOutside = position[0] < 0 or position[0] >= m
            xOutside = position[1] < 0 or position[1] >= n
            if xOutside or yOutside or matrix[position[0]][position[1]] != -1:
                position[0] -= direction[0]
                position[1] -= direction[1]

                direction = [direction[1], -direction[0]]

                position[0] += direction[0]
                position[1] += direction[1]
 
        # Return the resulting matrix
        return matrix