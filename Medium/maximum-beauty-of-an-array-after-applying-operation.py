# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        # First sort the numbers in ascending order
        nums.sort()

        # Then iterate a sliding window over
        maximum_beauty, start = 0, 0
        for end in range(n):
            # Shrink the window such that elements are beautiful
            while nums[start] < nums[end] - 2*k:
                start += 1

            # Remember current window size
            maximum_beauty = max(end - start + 1, maximum_beauty)
        
        # Finally, return the maximum beauty of the list
        return maximum_beauty
