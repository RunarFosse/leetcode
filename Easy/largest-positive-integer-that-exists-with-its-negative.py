# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Using sorting
        n = len(nums)

        # Sort nums list
        nums.sort()

        # Find the first largest positive number with a negative entry
        p1, p2 = 0, n-1
        while p1 < p2:
            if nums[p1] == -nums[p2]:
                return nums[p2]

            # Move pointers
            if nums[p1] < -nums[p2]:
                p1 += 1
            else:
                p2 -= 1

        # If no such number is found, return -1
        return -1