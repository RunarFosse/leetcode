# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        # Store the number of operations needed to turn
        # the current subarray into a non-decreasing one
        cost = 0

        # Keep track of modified plateaus in a monotonic queue
        plateaus = deque([])

        # Iterate the array from behind
        subarrays, end = 0, n
        for start in reversed(range(n)):
            # Merge plateaus with a height less than or equal to the current element
            while plateaus and nums[plateaus[0]] <= nums[start]:
                left = plateaus.popleft()
                right = plateaus[0] if plateaus else end

                # Adding the operation cost of raising these plateaus
                cost += (nums[start] - nums[left]) * (right - left)
            plateaus.appendleft(start)

            # If the cost to make this subarray non-decreasing ever exceeds k
            while cost > k:
                # Shrink the window
                cost -= nums[plateaus[-1]] - nums[end - 1]
                end -= 1

                # Removing any out-of-range plateaus
                if plateaus[-1] >= end:
                    plateaus.pop()
            
            # And counting all valid subarrays starting at this index
            subarrays += end - start
        
        # Finally, return the count of all such resulting subarrays
        return subarrays
