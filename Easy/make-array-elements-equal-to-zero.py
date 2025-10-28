# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Using prefix sum

        # Keep track of prefix sum variables as we go
        left, right = 0, sum(nums)
        
        # Then iterate the array
        valids = 0
        for num in nums:
            # If we are at a zero
            if not num:
                # Count the number of valid initial direction selections
                if left - right in [0, 1]:
                    valids += 1
                if right - left in [0, 1]:
                    valids += 1
            
            # And iterate the prefix sum
            left += num
            right -= num

        # Finally, return the number of valid selections
        return valids


# A starting position i is valid if the signed difference between the initial direction
# and the other direction is either one or zero. This makes the problem trivial.