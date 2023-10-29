# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Make both numbers equally sized (for cleaner code)
        n = max(len(a), len(b))
        if n == len(a):
            b = "0" * (n - len(b)) + b
        else:
            a = "0" * (n - len(a)) + a

        # Start adding
        number, carry = "", 0
        for i in reversed(range(n)):
            c1, c2 = a[i], b[i]

            if c1 == "1" and c2 == "1":
                if carry:
                    number = "1" + number
                else:
                    number = "0" + number
                    carry = 1
                continue
            
            if c1 == "1" or c2 == "1":
                if carry:
                    number = "0" + number
                else:
                    number = "1" + number
                continue

            if carry:
                number = "1" + number
                carry = 0
            else:
                number = "0" + number
        
        if carry:
            return "1" + number
        
        return number