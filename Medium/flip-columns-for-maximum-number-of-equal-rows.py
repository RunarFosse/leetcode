# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m)

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Using bit manipulation
        count = defaultdict(int)

        # Iterate every row
        for row in matrix:
            # Turn row into an integer
            bits = 0
            for bit in row:
                # But flip each bit if first bit is set
                bits = (bits << 1) + (bit ^ 1 if row[0] else bit)
        
            # And add to count
            count[bits] += 1

        # Return the maximum number of equal rows
        return max(count.values())

# Count and find the maximum number of rows which
# are congruent through a bit inversion operation.