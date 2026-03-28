# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # Using greedy
        n = len(lcp)

        # First, reconstruct the potential source string
        string, current = [None] * n, "a"
        for i in range(n):
            if string[i] is not None:
                continue

            # If the current character is outside the range, new string is not valid
            if ord(current) > ord("z"):
                return ""
            
            # Iterate the LCPs for this index
            for j in range(i, n):
                # If they share any common prefix, set to the current character
                if lcp[i][j]:
                    string[j] = current

            # And increment the current character
            current = chr(ord(current) + 1)

        # Afterwards, verify that the reconstructed string matches the given LCP matrix
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                # If the characters don't match
                if string[i] != string[j]:
                    # Verify that they also do not match in the LCP matrix
                    if lcp[i][j]:
                        return ""
                    continue
                
                # If they do match, and we are not at the end
                if i < n - 1 and j < n - 1:
                    # Verify that the current LCP is 1 longer than 1 index further
                    if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                        return ""
                    continue

                # Otherwise, ensure that the current LCP is 1
                if lcp[i][j] != 1:
                    return ""

        # If LCP check terminates, the string is valid so return
        return "".join(string)
