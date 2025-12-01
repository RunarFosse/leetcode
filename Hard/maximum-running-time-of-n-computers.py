# Author: Runar Fosse
# Time complexity: O(mlog k)
# Space complexity: O(1)

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Using binary search

        # Binary search the maximum running time of the computers
        left, right = 0, sum(batteries)
        while left < right:
            # Find the pivot as the middle value rounded up
            pivot = right - (right - left) // 2

            # Check if we can run computers for pivot time
            charge = 0
            for battery in batteries:
                # By using a single battery for up to pivot time
                charge += min(battery, pivot)

            # And move boundaries respectively
            if charge >= n * pivot:
                left = pivot
            else:
                right = pivot - 1

        # Return the maximum running time
        return left
