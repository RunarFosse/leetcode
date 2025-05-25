# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # First, count frequency of each word
        frequencies = defaultdict(int)
        for word in words:
            frequencies[word] += 1
        
        # Then, for every word
        length, middle = 0, 0
        for word in frequencies.keys():
            # If the word itself is palindromic
            if word[0] == word[1]:
                # Then count and add the number of pairs
                div, rem = divmod(frequencies[word], 2)
                length += 2 * div

                # And count a middle entry, if it exists
                middle |= rem

            # Otherwise, if the reversed word also exists
            elif word[::-1] in frequencies:
                # Then count the frequency of each
                current, other = frequencies[word], frequencies[word[::-1]]

                # And add the current number of palindromic pairs
                length += min(current, other)
        
        # Finally, return the longest palindrome length
        return 2 * (length + middle)

