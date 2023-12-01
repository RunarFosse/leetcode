# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    def isNumber(self, s: str) -> bool:
        # Lower all characters, and split on e
        parts = s.lower().split("e")

        # If there are more than 2 parts, it is not a valid number
        if len(parts) > 2:
            return False

        # If there is 2 parts, check that last part is an integer
        if len(parts) == 2:
            return self.isNumber(parts[0]) and self.isInteger(parts[1])
        
        # If there is only 1 part, check if it is a decimal or integer
        return self.isDecimal(parts[0]) or self.isInteger(parts[0])

    def isDecimal(self, s: str) -> bool:
        # Iterate string, checking that it follows decimal rules
        if not s:
            return False

        start = 1 if s[0] in ["+", "-"] else 0
        parts = s[start:].split(".")

        if len(parts) > 2:
            return False

        if len(parts) == 2:
            if not parts[0]:
                return self.isDigits(parts[1])
            if not parts[1]:
                return self.isDigits(parts[0])
            return self.isDigits(parts[0]) and self.isDigits(parts[1])

        return self.isDigits(parts[0])
    
    def isInteger(self, s: str) -> bool:
        # Iterate string, checking that it follows integer rules
        if not s:
            return False

        start = 1 if s[0] in ["+", "-"] else 0
        return self.isDigits(s[start:])

    def isDigits(self, s: str) -> bool:
        # Iterate string, checking they are all digits
        if not s:
            return False

        return all(c in digits for c in s)