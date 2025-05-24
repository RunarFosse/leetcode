# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Iterate every word
        indices = []
        for i, word in enumerate(words):
            # If it contains the character
            if x in word:
                # Append its index
                indices.append(i)

        # Finally, return every word index containing x
        return indices