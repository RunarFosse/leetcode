# Author: Runar Fosse
# Time complexity: O(n^22^n)
# Space complexity: O(n)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Using DFS
        self.s, self.n = s, len(s)
        self.seen = set()
        return self.dfs(0)

    def dfs(self, start: int) -> int:
        # Iterate every substring
        substring, max_substrings = "", 0
        for i in range(start, self.n):
            substring += self.s[i]

            # If the current substring is not already seen, split
            if substring not in self.seen:
                self.seen.add(substring)
                max_substrings = max(1 + self.dfs(i+1), max_substrings)
                self.seen.remove(substring)

        # Return the maximum number of substrings from here
        return max_substrings
    