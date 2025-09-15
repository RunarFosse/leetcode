# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Mark the broken letters as broken
        indexOf = lambda c: ord(c) - ord("a")
        broken = [False] * 26
        for c in brokenLetters:
            broken[indexOf(c)] = True

        # Then iterate every word
        typed = 0
        for word in text.split(" "):
            # If all characters can be typed, count it
            if all(not broken[indexOf(c)] for c in word):
                typed += 1
        
        # Finally, return the number of words that can be typed
        return typed