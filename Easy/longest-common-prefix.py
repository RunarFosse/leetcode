# Author: Runar Fosse
# Time complexity: O(n*m)
# Space complexity: O(m)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            if len(str) < len(prefix):
                prefix = prefix[:len(str)]

            for j in range(0, len(str)):
                if j >= len(prefix):
                    break
                if prefix[j] != strs[i][j]:
                    prefix = prefix[0:j]
                    break

        return prefix