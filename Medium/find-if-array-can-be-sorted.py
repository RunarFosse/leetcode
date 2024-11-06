# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        # Iterate the array
        i, last_max = 0, 0
        while i < n:
            current_max, set_bits = 0, nums[i].bit_count()
            # Iterate the subarray of equal set bits
            while i < n and nums[i].bit_count() == set_bits:
                # If there is a number which is smaller than last
                # subarrays max, the array cannot be sorted
                if nums[i] < last_max:
                    return False

                current_max = max(nums[i], current_max)
                i += 1
            
            # Store the current max and move on to the next subarray
            last_max = current_max
        
        # If loop has terminated, array can be sorted
        return True
