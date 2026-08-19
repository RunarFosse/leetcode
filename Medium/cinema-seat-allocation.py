# Author: Runar Fosse
# Time complexity: O(m)
# Space complexity: O(m)

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Using bit manipulation
        m = len(reservedSeats)

        # Store each four-person seat allocation using bits
        block1 = 0b11110
        block2 = block1 << 2
        block3 = block2 << 2

        # Iterate each reservation
        rows = defaultdict(lambda: (1 << 10) - 1)
        for row, seat in reservedSeats:
            # Marking reserved spots
            rows[row - 1] -= 1 << (seat - 1)

        # Then, iterate each of these rows
        groups = 0
        for reserved in rows.values():
            # Check if each of the seat allocations can be sat in this row
            free1 = (reserved & block1) == block1
            free2 = (reserved & block2) == block2
            free3 = (reserved & block3) == block3

            # And check if we can sit two, or one four-person groups
            if free1 and free3:
                groups += 2
            elif free1 or free2 or free3:
                groups += 1
        
        # Additionally, count all groups that can be sat in fully free rows
        frees = n - len(rows)
        groups += 2 * frees
        
        # Finally, return this maximum number of four-person groups we can sit
        return groups
