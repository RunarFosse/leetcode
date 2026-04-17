# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Iterate the numbers
        minimum, mirrors = 1e9, {}
        for i, num in enumerate(nums):
            # Check if the current number has been seen before
            if num in mirrors:
                # Store the minimum distance
                distance = i - mirrors[num]
                minimum = min(distance, minimum)

            # Then, compute the mirror of the current number and store the index
            mirror = self.reverse(num)
            mirrors[mirror] = i
        
        # Finally, return the minimum absolute distance between mirror pairs, if it exists
        return minimum if minimum < 1e9 else -1
        
    def reverse(self, num: int) -> int:
        # Reverse the digits of a given number
        reverse = 0
        while num:
            reverse *= 10
            reverse += num % 10
            num //= 10
        
        return reverse
