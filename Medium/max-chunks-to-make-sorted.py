# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Iterate the array
        chunks, maximum = 0, 0
        for i, num in enumerate(arr):
            # Store current chunk maximum
            maximum = max(num, maximum)

            # If the index equals the maximum, then we can sort chunk
            if i == maximum:
                chunks += 1
        
        # Return the maximum number of chunks
        return chunks
