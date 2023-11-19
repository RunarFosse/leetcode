# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Count frequency of each number
        n = len(nums)
        max_num = max(nums)
        min_num = max_num

        sorted_nums = [0] * n
        counts = [0] * max_num
        for num in nums:
            counts[num-1] += 1
            min_num = min(num, min_num)

        # Use the calculated frequency to compute total needed operations
        total_operations, cumulative_operations = 0, 0
        for i in reversed(range(min_num, max_num)):
            if counts[i] != 0:
                cumulative_operations += counts[i]
                total_operations += cumulative_operations

        return total_operations

# Total number of steps needed is sum of how many steps needed per number, which is equal to
# "distance" from smallest number. This can easily be computed, as we already have the counts
# from doing counting sort. Summing the counts up from the largest number will give us the
# cumulative number of operations needed to make all current numbers equal to the smallest.