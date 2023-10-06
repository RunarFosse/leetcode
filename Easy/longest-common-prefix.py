# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(m)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Using lexicographical sorting
        strs.sort()

        prefix_index = 0 if len(strs[0]) < len(strs[-1]) else -1
        other_index = abs(prefix_index) - 1

        prefix = ""
        for i in range(0, len(strs[prefix_index])):
            if strs[prefix_index][i] != strs[other_index][i]:
                break
            prefix += strs[prefix_index][i]
        
        return prefix