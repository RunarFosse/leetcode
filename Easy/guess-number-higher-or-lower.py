# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Using binary search
        left, right = 0, n+1
        while left < right:
            pivot = (left+right) // 2
            result = guess(pivot)

            # Correct guess, return
            if result == 0:
                return pivot
            # If not, modify bounds respectively
            elif result == 1:
                left = pivot
            else:
                right = pivot

        # If we escape loop, correct guess has to be the upperbound
        return right