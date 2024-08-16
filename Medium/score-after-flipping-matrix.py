# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Using greedy
        m, n = len(grid), len(grid[0])

        # Iterate every column
        result = 0
        for j in range(n):
            # Count set bits in column
            set_bits = sum(1 for i in range(m) if grid[i][j] == grid[i][0])

            # Check if we should flip column
            set_bits = max(m - set_bits, set_bits)

            # Add current binary sum to result
            result += set_bits * (1 << n-j-1)
            
        # Return the final row sum
        return result

        
# The matrix is scored by interpretting the rows as binary numbers.
# A binary number can be maximized by ensuring beginning digits are set to 1.
# E.g. the binary number 1XX.. is always bigger than the complement 0YY,
# regardless of the value of XX/YY.

# Therefore we can greedily solve this by ensuring all rows have a set digit
# in the starting column, then columnwise flip each column if the number of
# 0s in each row is larger than the number of 1s.

# At last we parse the rows and return the sum.

# We can also calculate the sum on the fly, when columnwise flipping, keeping
# count of the flipped rows. This is done by "assuming" the first value in
# every row is a set bit. Then we can compare the value of each bit with
# its respective first bit. If they are equal, we count them as set.