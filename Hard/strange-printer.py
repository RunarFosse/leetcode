# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(n^2)

class Solution:
    def strangePrinter(self, s: str) -> int:
        # Using dynamic programming

        # First remove consecutive duplicate letters from the string
        chars = [""]
        for c in s:
            if c != chars[-1]:
                chars.append(c)
        self.s = "".join(chars)

        # Then perform dynamic programming
        return self.opt(0, len(self.s))
    
    @functools.cache
    def opt(self, start: int, end: int) -> int:
        if start >= end:
            return 0
        
        # Set initial number of turns as worst case
        # printing every letter one by one
        turns = 1 + self.opt(start + 1, end)

        # Check if we can optimize by grouping prints together,
        # if we find letters equal to current
        for i in range(start + 1, end):
            if self.s[i] != self.s[start]:
                continue

            split = self.opt(start, i) + self.opt(i + 1, end)
            turns = min(split, turns)

        # Return minimum number of turns
        return turns


# opt(start, end) - Minimum number of turns to print the string s[start:end]

# Base case:
# opt(start >= end, end) = 0

# Recurrency:
# opt(start, end) = min(
#                  1 + opt(start + 1, end),
#                  1 + opt(start + 1, i) + opt(i + 1, end) 
#                  for i in range(start + 1, end)  
#                  if s[start] == s[i]
#)

# N.o. states = n^2
# Runtime per state = O(n)
# => Final time complexity of O(n^3)