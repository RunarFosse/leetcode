# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = 0
        for i in range(n):
            # Check if current char is a vowel
            if s[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                # Add/subtract depending on current partition
                vowels += 1 if i < n // 2 else -1
        
        # Verify that final count is 0
        return vowels == 0

# We can count vowels in each string partition. If we count the number of 
# vowels in the first partition, and subtract the number of vowels in the 
# second partition, then the string halves will be alike if and only if
# the total count at the end is 0.