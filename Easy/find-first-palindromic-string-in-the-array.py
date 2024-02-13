# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Using two pointer approach
        for word in words:
            # Check if first and last character matches
            # iterating through the word
            s, e = 0, len(word)-1
            isPalindrome = True
            while s <= e:
                # If they don't, string is not palindromic
                if word[s] != word[e]:
                    isPalindrome = False
                    break
                s += 1
                e -= 1

            if isPalindrome:
                return word
            
        return ""


# Iterate each word, returning it if it is a palindrome.