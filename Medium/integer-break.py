# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def integerBreak(self, n: int) -> int:
        # Using the observation that 3**n > n**3 for all n>0

        if n <= 3:
            return ceil(n/2) * floor(n/2)
        
        div, rem = divmod(n, 3)
        if rem == 1:
            rem += 3
            div -= 1
        
        return pow(3, div) * (rem if rem else 1)