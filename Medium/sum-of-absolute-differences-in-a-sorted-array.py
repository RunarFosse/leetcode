# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        differences = []

        # Precalculate absolute difference sum for first entry
        differences.append(sum(abs(nums[0] - num) for num in nums))

        # Then for each other entry, build upon this precalculated sum
        for i in range(1, n):
            prev_diff = abs(nums[i-1] - nums[i])
            
            right_add = prev_diff * i
            left_remove = prev_diff * (n - i)

            differences.append(differences[i-1] + right_add - left_remove)

        return differences