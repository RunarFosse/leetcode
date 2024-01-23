# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # First turn into numbers
        self.strings = []
        for string in arr:
            bits = 0
            valid = True
            for c in string:
                # Verify string contains no duplicates
                if bits >> ord(c) - ord("a") & 1:
                    valid = False
                    break
                # If not, set the current bit
                bits |= pow(2, ord(c) - ord("a"))
            
            if valid:
                self.strings.append(bits)
        
        # Then perform DFS, finding the longest string with unique characters
        self.n = len(self.strings)
        return self.dfs(0, 0)

    def dfs(self, index: int, bits: int) -> int:
        # Start with max_length initialized at current string length
        max_length = bits.bit_count()
        
        # Then check if any other possible concatenations leads to longer string
        for i in range(index, self.n):
            if bits & self.strings[i]:
                continue
            max_length = max(self.dfs(i+1, bits | self.strings[i]), max_length)
            
        # Return the maximum length
        return max_length

# First we turn each string in arr into number form, where bit i is set to 1 if
# the string contains letter i. Whilst doing this we also prune strings in arr
# containing duplicate characters.