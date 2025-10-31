# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Using bitmask

        # Iterate the array
        seen, duplicates = 0, []
        for num in nums:
            # If we've seen the number before, add it to the array
            if seen & 1 << (num + 1):
                duplicates.append(num)

            # Storing the seen numbers in a bitmask
            seen |= 1 << (num + 1)
        
        # Finally, return the two duplicates
        return duplicates
    