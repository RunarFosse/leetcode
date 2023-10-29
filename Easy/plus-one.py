# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = digits.copy()
        for i in reversed(range(0, len(digits))):
            number[i] = (number[i] + 1) % 10

            if number[i]:
                return number

        return [1] + number