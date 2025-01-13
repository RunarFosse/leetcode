# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If length of string is odd, string cannot be valid
        n = len(s)
        if n % 2:
            return False

        # First iterate string from left to right, counting open parantheses
        opened = 0
        for i in range(n):
            if s[i] == "(" or locked[i] == "0":
                opened += 1
            else:
                opened -= 1
            
            # If there are more closed than opened, string is invalid
            if opened < 0:
                return False
        
        # Then iterate right-to-left, counting closed parantheses
        closed = 0
        for i in reversed(range(n)):
            if s[i] == ")" or locked[i] == "0":
                closed += 1
            else:
                closed -= 1
            
            # If there are more opened than closed, string is invalid
            if closed < 0:
                return False
        
        # If both loops terminate, string is valid!
        return True