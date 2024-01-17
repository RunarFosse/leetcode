# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = ""
        # For each row
        for j in range(numRows):
            # Find current column letter
            for i in range(0, len(s)-j, 2*(numRows-1)):
                zigzag += s[i+j]
                # And add next diagonal letter if supposed to
                next_diagonal = i+2*(numRows-1) - j
                if j > 0 and j < numRows - 1 and next_diagonal < len(s):
                    zigzag += s[next_diagonal]
            
        return zigzag
        
# If the number of rows given are 1, the result will be the input string s.

# Otherwise we see that the index of the letters in the first row are equal to
# integer multiples of 2*(numRows-1).

# Likewise, the second row is equal to 2*(numRows-1)+1, the third 2*(numRows-1)+2,
# etc., up until row numRows which is 2*(numRows-1)+numRows-1 = 3*(numRows-1).

# We also need to remember the diagonal sections, which are written only at
# rows in the middle (1 < diagonals < numRows). For row j, the diagonal letter
# on the current row is given as the current i (=2*(numRows-1)) 
# + 2*(numRows-1) - j. (Calculated from next "whole column"'s letter backtracking
# back to current diagonal letter).


# As we only traverse each letter at most once, this has time complexity O(n).