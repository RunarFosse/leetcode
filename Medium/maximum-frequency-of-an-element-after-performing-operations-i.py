# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Using greedy

        # Count the frequency of each number, storing minimum and maximum entry
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1

        # Sort the array in ascending order
        nums.sort()
        
        # And, for each number, compute frequency after applying operations
        maximum = 0
        for num in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, num - k)
            right = bisect_right(nums, num + k)
            frequency = min(right - left, frequencies[num] + numOperations)
            maximum = max(frequency, maximum)

        # Finally, return the maximum frequency
        return maximum
