# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.n, self.s, self.i = len(s), s, 0
        return self.parse(False)
    
    def parse(self, reverse: bool) -> str:
        # Keep track of current substring
        substring = []

        # Iterate from current index
        while self.i < self.n:
            # If we ever meet an open paranthesis, recurse
            if self.s[self.i] == "(":
                self.i += 1
                substring.append(self.parse(not reverse))
                continue
            
            # If we meet a closed, break current recursion
            if self.s[self.i] == ")":
                self.i += 1
                return "".join(reversed(substring) if reverse else substring)
            
            # If not, add next char and continue iteration
            substring.append(self.s[self.i])
            self.i += 1

        # If we reach the end, return
        return "".join(reversed(substring) if reverse else substring)