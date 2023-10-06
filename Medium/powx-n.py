# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Using binary exponentiation

        if n < 0: # 2^-5 = (2^-1)^5
            return self.myPow(1/x, -n)

        if n == 0:
            return 1
        
        if n % 2:
            return self.myPow(x, n - 1) * x
        
        res = self.myPow(x, n / 2)
        return res * res
