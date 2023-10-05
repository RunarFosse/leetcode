# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window solution
        memo = set()
        start = 0
        length, maxlength = 0, 0
        for i, c in enumerate(s):
            if memo.issuperset({c}):
                maxlength = max(length, maxlength)

                while s[start] != c:
                        memo.discard(s[start])
                        start += 1
                        length -= 1
                start += 1
                continue
            
            length += 1
            memo.add(c)

        return max(length, maxlength)