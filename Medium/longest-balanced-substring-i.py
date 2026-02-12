# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # Iterate every subarray
        maximum = 0
        for i in range(n):
            frequencies = defaultdict(int)
            for j in range(i, n):
                # Count the frequency of the current character
                frequencies[s[j]] += 1

                # If the current substring is balanced, store maximum subarray size
                if max(frequencies.values()) == min(frequencies.values()):
                    maximum = max(j - i + 1, maximum)
        
        # Finally, return this said maximum balanced substring size
        return maximum
