# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using two pointer approach
        
        # We check if the remaining string is a palindrome
        # If any character is non-alphanumeric, skip it
        start, end = 0, len(s)-1
        while start <= end:
            # Skip any non-alphanumeric characters
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
        
        return True