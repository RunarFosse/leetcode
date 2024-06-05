# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(1)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize initial character frequency list
        frequencies = [100] * 26

        # Then for each word, compare frequency lists of word with initial 
        # and combine by substituting minimum value.
        for word in words:
            word_frequencies = self.countFrequencies(word)
            for i in range(26):
                frequencies[i] = min(frequencies[i], word_frequencies[i])

        # Then at last, return list containing each character explicitly
        return [chr(i + ord("a")) for i in range(26) for _ in range(frequencies[i])]

    def countFrequencies(self, word: str) -> List[int]:
        indexOf = lambda c : ord(c) - ord("a")
        frequencies = [0] * 26
        for c in word:
            frequencies[indexOf(c)] += 1

        return frequencies