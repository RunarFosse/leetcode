# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        max_sum, current_sum = 0, 0
        start, indices = 0, defaultdict(lambda: -1)
        for i in range(n):
            # Ensure elements in subarray stay distinct and has size k
            while start <= indices[nums[i]] or i - start > k - 1:
                current_sum -= nums[start]
                start += 1
            
            current_sum += nums[i]
            indices[nums[i]] = i
            
            # If subarray has size k, remember sum
            if i - start == k - 1:
                max_sum = max(current_sum, max_sum)

        # Return maximum sum of subarray
        return max_sum
