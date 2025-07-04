# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Using binary search

        # Simulate the operations from end-to-start
        offset, i = 0, len(operations) - 1
        while k > 1:
            # If k is in the right part
            if k > (1 << i):
                # Add the current operation
                offset = (offset + operations[i]) % 26
                k -= (1 << i)
            i -= 1
        
        # Finally, return the k'th character
        return chr(offset + ord("a"))
    