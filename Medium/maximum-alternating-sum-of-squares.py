# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # First, sort the numbers in ascending order of absolute value
        nums.sort(key=lambda e: abs(e))

        # Then, greedily add large and subtract small
        score, left, right = 0, 0, (n - 1)
        while left <= right:
            # Add the square of the current largest element
            score += nums[right] * nums[right]
            right -= 1

            # If not already used, subtract the square of the current smallest element
            if left <= right:
                score -= nums[left] * nums[left]
                left += 1
        
        # Finally, return this maximum possible alternating score
        return score
