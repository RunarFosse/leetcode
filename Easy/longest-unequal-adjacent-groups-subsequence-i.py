# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Greedily create the longest alternating subsequence
        sequence, last = [], -1
        for word, group in zip(words, groups):
            if group != last:
                sequence.append(word)
                last = group

        # Finally, return the subsequence
        return sequence