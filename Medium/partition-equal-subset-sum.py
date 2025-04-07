# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Iterate the array
        sums, total = 1, 0
        for num in nums:
            # Computing total sum of array
            total += num

            # And sum of all subsets in the array
            sums |= sums << num
        
        # If there exists a subset sum equal to half the total, return True
        return not total % 2 and sums & 1 << (total // 2) != 0
