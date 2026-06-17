# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def processStr(self, s: str, k: int) -> str:
        # First, compute the length of the resulting string
        length = 0
        for c in s:
            # Given the current character, apply its respective operation
            match c:
                # Either remove the last character from result
                case '*':
                    length = max(length - 1, 0)
                # Duplicate and append the current result
                case '#':
                    length *= 2
                # Reverse the current result
                case '%':
                    pass
                # Or append the current character
                case _:
                    length += 1
        
        # Return early if the resulting string length is smaller than k
        if length < k + 1:
            return '.'
        
        # Then, traverse the string backwards
        for c in reversed(s):
            # Reverting all operations to the resulting string
            match c:
                case '*':
                    length += 1
                case '#':
                    length -= length // 2
                    # When duplicating string, and k is on the 'new' side
                    if length < k + 1:
                        # Update k to be reflected to the 'old' side
                        k -= length
                case '%':
                    # When reversing, we only update the position of k
                    k = length - k - 1
                case _:
                    # If we finally find the k'th character, return it
                    if length == k + 1:
                        return c
                    length -= 1
