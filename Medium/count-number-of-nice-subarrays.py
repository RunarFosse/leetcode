# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)
        subarrays = 0

        # Expand a window until it contains k odd numbers
        start, end = -1, 0
        first_odd = -1
        while end < n:
            # If number is odd, decrement k
            if nums[end] % 2:
                k -= 1
            
            # If k ever becomes negative, shrink window until k is 0
            while k < 0:
                start += 1
                if nums[start] % 2:
                    k += 1

            # Whenever k is 0, count possible nice subarrays
            if not k:
                # This is done by counting number of even
                # numbers at the beginning of the window
                while first_odd == start or not nums[first_odd] % 2:
                    first_odd += 1
                
                # And computing number of nice subarrays given the new number
                subarrays += (first_odd - start)
            
            # Finally expand window
            end += 1

        # Return number of possible nice subarrays
        return subarrays
