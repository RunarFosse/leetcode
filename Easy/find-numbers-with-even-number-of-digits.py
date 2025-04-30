# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Iterate the numbers
        count = 0
        for num in nums:
            # Count it if it has an even number of digits
            digits = int(log10(num)) + 1
            if not digits % 2:
                count += 1
        
        return count