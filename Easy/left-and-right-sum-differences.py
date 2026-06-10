# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Using prefix sum
        n = len(nums)

        # Initialize the array with each index's prefix sum
        answer, prefix = [], 0
        for i in range(n):
            answer.append(prefix)
            prefix += nums[i]
        
        # Then, replace each element with the different of its suffix sum
        suffix = 0
        for i in reversed(range(n)):
            answer[i] = abs(answer[i] - suffix)
            suffix += nums[i]
        
        # Finally, return this resulting answer array
        return answer
