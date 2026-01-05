# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Using Knuth-Morris-Pratt
        length = self.kmp(s)

        # Combine non-palindromic suffix of s to make a palindrome, and return
        palindrome = s[length:][::-1] + s
        return palindrome

    def kmp(self, string: str) -> int:
        # Compute the longest palindromic prefix of string

        # First, combine the two strings with a separator
        combined = string + "#" + string[::-1]

        # Then, store longest length of prefixes in pattern that are suffixes string
        matching = [0] * len(combined)

        # Then, iterate this new string with a two pointer approach
        i, j = 1, 0
        while i < len(combined):
            # If two the characters match
            if combined[i] == combined[j]:
                # Mark as matching and extend our search
                j += 1
                matching[i] = j
                i += 1
            else:
                # Otherwise, if we have a smaller matching prefix, continue from there
                if j > 0:
                    j = matching[j - 1]
                else:
                    # If not, restart from the next index
                    matching[i] = 0
                    i += 1
        
        # Finally, return the length of the longest palindromic prefix of string
        return matching[-1]
