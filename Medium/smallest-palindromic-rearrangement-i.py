# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # First, count the frequency of each character
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Then, construct the lexicographically smallest palindrome
        first, middle = [], ""
        for i in range(26):
            # If we find a odd frequency, this is our middle character
            if frequencies[i] % 2:
                middle = chr(i + ord("a"))
                frequencies[i] -= 1
            
            # And half of every character to the first half of the string
            first.extend([chr(i + ord("a"))] * (frequencies[i] // 2))
        
        # Then construct palindrome by adding middle and appending first half reversed
        return "".join(first + [middle] + first[::-1])
