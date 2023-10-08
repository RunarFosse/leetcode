# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy algorithm
        
        jumps, end, reach = 0, 0, 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if end == i:
                jumps += 1
                end = reach
                if end >= len(nums) - 1:
                    break

        return jumps