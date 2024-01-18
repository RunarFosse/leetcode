# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Using two pointer approach
        n = len(nums)
        closest = 1e9

        # Initially sort the nums array
        nums.sort()
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                # Store the closest sum
                sum = nums[i] + nums[j] + nums[k]
                if abs(target - sum) < abs(target - closest):
                    closest = sum
                
                # Shrink the window based on relative size of sum
                if sum < target:
                    j += 1
                else:
                    k -= 1

        return closest
        
# Sorting has space complexity O(n), thus leading to final SC.
# Time complexity is dominated by nested loops.