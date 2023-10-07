# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(nm)

class Solution:
    def countAndSay(self, n: int) -> str:
        # Using Dynamic programming
        return self.opt(n)
    
    def opt(self, n: int) -> str:
        if n == 1:
            return "1"
        
        rec = self.opt(n-1)
        message = ""
        # Count frequencies of characters
        curr, freq = "", 0
        for c in rec:
            if c == curr:
                freq += 1
            else:
                if freq:
                    message += str(freq) + curr
                curr = c
                freq = 1
        message += str(freq) + curr
        
        return message


# Base case:
# opt(1) = "1"

# Recurrency:
# opt(i) = say opt(i-1)
# where say gives: (c_i is character of index i, f_i is frequency of c_i)
# f_i + c_i

# N.o. states = O(n)
# Runtime per state = O(m)