# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Using binary search
        n = len(chalk)

        # First calculate a prefix sum array
        prefix = []
        for i in range(n):
            prefix.append(prefix[-1] + chalk[i] if prefix else chalk[i])

        # Then we can figure out who replaces the chalk in the last pass
        # using binary search
        remainder = k % prefix[-1]
        left, right = 0, n
        while left < right:
            pivot = (left + right) // 2

            # If pivot student uses up the chalk, next student has to replace
            if prefix[pivot] == remainder:
                return pivot + 1

            # If not, move pointers accordingly
            if prefix[pivot] < remainder:
                left = pivot + 1
            else:
                right = pivot
        
        return left
            