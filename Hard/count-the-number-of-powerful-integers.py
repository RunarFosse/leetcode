# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Using combinatorics
        upToFinish = self.countPowerfulUpTo(finish, limit, s)
        upToStart = self.countPowerfulUpTo(start - 1, limit, s)
        return upToFinish - upToStart
        
    def countPowerfulUpTo(self, x: int, limit: int, s: str) -> int:
        # First, stringify x
        x = str(x)
        if len(x) <= len(s):
            return 0 if len(x) < len(s) or x < s else 1
        
        # Then iterate the prefix of the number from the left
        powerful, prefix = 0, len(x) - len(s)
        for i in range(prefix):
            # If the current digit is bigger than the limit
            if int(x[i]) > limit:
                # Count all permutations less than the limit and return
                powerful += pow(limit + 1, prefix - i)
                return powerful
            
            # If not, count all permutations up to the current digit
            powerful += int(x[i]) * pow(limit + 1, prefix - i - 1)
        
        # If the suffix of the number ends with a possible s, count it
        if x[prefix:] >= s:
            powerful += 1
        
        # Finally, return the number of powerful integers
        return powerful