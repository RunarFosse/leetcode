# Author: Runar Fosse
# Time complexity: O(4^n)
# Space complexity: O(n2^n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Exponential time algorithm
        strings = []
        for i in range(1, pow(4, n)+1):
            if i.bit_count() != n: # Not equal 0s and 1s
                continue
            
            opened, closed = 0, 0
            string = ""
            while i:
                if i & 1:
                    closed += 1
                    string = ")" + string
                else:
                    opened += 1
                    string = "(" + string
                
                if opened > closed:
                    break
                i >>= 1

            # Number might start with 0s, e.g. 000111
            string = "(" * (closed - opened) + string
            
            if not i:
                strings.append(string)

        return strings

# Bit string analogous to string
# 0 -> Open paranthesis, 1 -> Closed

# Iterate all bit strings from 1 (0 obviously invalid) to 2^(2n) = 4^n
# Check if a bit string is a valid paranthesis string, if so store it

# A bit string is valid if:
# No. 1s and 0s in the number are equal (and is n)
# reading from right, all 0s have equal no. 1s to the right