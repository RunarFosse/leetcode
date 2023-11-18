# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Using counting sort, prefix sum and sliding window
        n = len(nums)
        max_num = max(nums)

        # Sort nums in ascending order
        counts = [0] * max_num
        for num in nums:
            counts[num-1] += 1
        for i in range(1, max_num):
            counts[i] += counts[i-1]
        
        sorted_nums = [0] * n
        for num in nums:
            sorted_nums[counts[num-1]-1] = num
            counts[num-1] -= 1
        
        # Calculate prefix sum
        prefix, sum = [], 0
        for num in sorted_nums:
            prefix.append(sum)
            sum += num

        # Sliding window
        maximum_frequency = 1
        left, right = 0, 1
        while right < n:
            window_size = right - left
            current_sum = prefix[right] - prefix[left]
            pivot = sorted_nums[right]

            if current_sum + k < pivot * window_size:
                left += 1
            else:
                maximum_frequency = max(window_size+1, maximum_frequency)
                right += 1
        
        return maximum_frequency

# Note: n in time complexity represents maximum entry in nums
# However, as '1 <= nums.length <= 10^5' and '1 <= nums[i] <= 10^5' they are practically
# equivalent in complexity terms.