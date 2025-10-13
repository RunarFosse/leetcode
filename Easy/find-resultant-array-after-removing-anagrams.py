# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Iterate every word
        array, frequencies = [], None
        for word in words:
            # If the word's frequencies does not match the previous'
            current = self.countFrequencies(word)
            if current != frequencies:
                # Add the current word to the array, and update frequencies
                array.append(word)
                frequencies = current

        # Finally, return the resulting array
        return array
        
    def countFrequencies(self, word: str) -> List[int]:
        # Count the frequency of each letter in the word
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("a")

        for c in word:
            frequencies[indexOf(c)] += 1
        return frequencies