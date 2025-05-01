# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Iterate every possible number
        symmetric = 0
        for num in range(low, high + 1):
            # Check if it has an even number of digits
            digits = int(log10(num)) + 1
            if digits % 2:
                continue
            
            # Then compute the left and right digit sums
            left, right = 0, 0
            for i in range(digits):
                if i < digits // 2:
                    right += num % 10
                else:
                    left += num % 10
                num //= 10
            
            # If they are equal, count it as symmetric
            if left == right:
                symmetric += 1
        
        # Finally, return the number of symmetric integers in the range
        return symmetric