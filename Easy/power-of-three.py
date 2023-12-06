# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      if n <= 0:
        return False
      
      # To prevent numerical errors when computing logarithms we perform a small rounding
      logarithm = log(n, 3)
      logarithm = round(logarithm * 1e9)
      logarithm /= 1e9

      # Is true if log has no decimals
      return not logarithm % 1
        
# n is a power of 3 if log_3(n) is an integer. Obviously only for n >= 0