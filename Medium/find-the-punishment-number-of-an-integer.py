# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(log m)

# where m is the maximum size of a number

class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Iterate every i from [1, n]
        punishment = 0
        for i in range(1, n + 1):
            # If the square has digits which can be partitioned sum to i
            square = i * i
            if self.hasPartitionSum(square, i):
                # Then add it to the punishment number
                punishment += square

        # Return the punishment number
        return punishment
    
    def hasPartitionSum(self, square: int, i: int) -> bool:
        # See if we should return early
        if square <= i or i < 0:
            return square == i
            
        # Otherwise, backtrack 
        current, multiplier = 0, 1
        while square:
            current += (square % 10) * multiplier
            square //= 10
            multiplier *= 10
            if self.hasPartitionSum(square, i - current):
                return True
        
        # If we find no equal partition sum, return false
        return False