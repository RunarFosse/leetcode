# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        # Using binary search
        if x <= 1:
            return x

        left, right = 0, x
        while left < right:
            pivot = (left + right) // 2

            square = pivot*pivot
            if square == x:
                return pivot

            if square < x:
                if pivot == left:
                    break
                left = pivot
            else:
                right = pivot

        return left