# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # Iterate the bitstring
        flips = 0
        for i in range(n):
            # If an element is 0
            if not nums[i]:
                # If we are at the last 2 elements, we cannot flip :/
                if i+3 > n:
                    return -1

                # Bit flip it and the 2 elements directly following it
                for j in range(3):
                    nums[i+j] ^= 1
                
                # Increment the bit flip counter
                flips += 1
        
        # Return the number of flips
        return flips


# Greedily flip the first bit if it is equal to 0 and iterate. We then do this
# until we reach the end of the array. If the result is that all elements are
# equal to 1, return the number of flips. If not, return -1.