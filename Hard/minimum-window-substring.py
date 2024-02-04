# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Using sliding window
        if len(s) < len(t):
            return ""
        
        # Count characters in t
        chars = defaultdict(int)
        for c in t:
            chars[c] += 1
        
        # Sliding window over s
        start, end = 0, 0
        substring = None
        check = True        # reduces redundant iteration over chars.values()
        while start <= end:
            # Need more characters in window
            if check and any(val > 0 for val in chars.values()):
                # Break if window exceeds the end
                if end == len(s):
                    break
                
                # Increment end pointer
                c = s[end]
                if c in chars:
                    chars[c] -= 1
                end += 1

            else:
                check = False
                # Store substring if it is minimal
                if not substring or substring[1] - substring[0] > end - start:
                    substring = (start, end)
                
                # Increment start pointer
                c = s[start]
                if c in chars:
                    chars[c] += 1
                    if chars[c] > 0:
                        check = True
                start += 1
        
        # If we have found a substring, return it
        if substring:
            return s[substring[0]:substring[1]]

        # If not, return empty string
        return ""

# As the strings only can contain upper and lowercase english characters,
# the dictionary size is upper bounded by size 2*26 = 52. This means that
# both the storage and runtime of iterating through every hashmap value is O(1).
# As the first for loop is O(m), second is O(n), we get a final time
# complexity of O(m + n).

# Note that space complexity is overruled by the string slice at the end,
# which is at most sized len(t) == m.