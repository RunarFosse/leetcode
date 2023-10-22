# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Using greedy algorithm
        n = len(nums)
        currentmin = score = nums[k]
        if currentmin < 0:
            return score
        
        left, right = k, k
        while left > 0 or right < n-1:
            # Check if any left or right is bigger than or equal to
            # current min, if so, freely add them
            while left > 0 and nums[left-1] >= currentmin:
                left -= 1
            while right < n-1 and nums[right+1] >= currentmin:
                right += 1
            
            # Update score
            score = max(currentmin * (right - left + 1), score)
            
            # If not, pick the biggest number and add it to the subarray
            canleft, canright = left > 0, right < n-1
            if canleft and (not canright or nums[left-1] > nums[right+1]):
                left -= 1
                currentmin = nums[left]
            elif canright:
                right += 1
                currentmin = nums[right]

        return score