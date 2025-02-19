# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Using backtracking
        string, self.k = [""], k
        self.backtrack(n, string)
        return "".join(string)

    def backtrack(self, i: int, previous: List[str]) -> None:
        # If we are at the end, decrement k and return
        if not i:
            self.k -= 1
            return 
        
        # If not, iterate characters
        for c in "abc":
            # Skip if equal to previous
            if c == previous[-1]:
                continue
            
            # If not, add and continue
            previous.append(c)
            self.backtrack(i - 1, previous)

            # If k is 0, we have our string
            if not self.k:
                return
            
            # Otherwise, remove character and continue
            previous.pop()
