# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestBalanced(self, s: str) -> int:
        # Using prefix sum
        n = len(s)

        # First, handle the case of only 1 distinct character
        maximum, current = 1, 1
        for i in range(1, n):
            # Count length of consecutive homogeneous substrings
            if s[i] != s[i - 1]:
                current = 1
            else:
                current += 1
            maximum = max(current, maximum)

        # Next, handle the case of 2 distinct characters
        for exception in "abc":
            primary = None
            first, prefix = {0: -1}, 0
            for i in range(n):
                # If we ever find the 3rd exception character, restart counting
                if s[i] == exception:
                    first, prefix = {0: i}, 0
                    continue
                
                # Mark the first occuring non-exception character
                if primary is None:
                    primary = s[i]
                
                # And count the current balance of either of these characters
                prefix += 1 if s[i] == primary else -1
                if prefix in first:
                    maximum = max(i - first[prefix], maximum)
                else:
                    first[prefix] = i

        # Lastly, handle the case with 3 distinct characters
        first, prefix = {0: -1}, 0
        for i in range(n):
            # Store a balance prefix as a sum which only is 0 if substring is balanced
            if s[i] == "a":
                prefix += (1 << 17) + 1
            elif s[i] == "b":
                prefix -= (1 << 17)
            else:
                prefix -= 1

            # Storing the longest such balanced substring
            if prefix in first:
                maximum = max(i - first[prefix], maximum)
            else:
                first[prefix] = i
        
        # Finally, return the maximum balanced substring size
        return maximum
