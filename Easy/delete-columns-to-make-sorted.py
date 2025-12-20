# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # First, transpose the grid to get a list of columns
        transposed = zip(*strs)

        # Then iterate those columns
        deleted = 0
        for column in transposed:
            # If it is not in lexicographical order
            if any(map(lambda pair: pair[0] > pair[1], pairwise(column))):
                # Then delete it
                deleted += 1
        
        # Return the number of deleted columns
        return deleted

# As we are using iterators, space complexity stays constant!