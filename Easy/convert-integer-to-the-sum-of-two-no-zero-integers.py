# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Then, while either contains a zero
        left, right = 1, n - 1
        while self.hasZero(left) or self.hasZero(right):
            # Increment left while decrementing right
            left += 1
            right -= 1
        
        # Finally, return the two non-zero integers
        return [left, right]

    def hasZero(self, i: int) -> bool:
        # Check if the given integer contains a zero
        while i:
            if i % 10 == 0:
                return True
            i //= 10
        return False