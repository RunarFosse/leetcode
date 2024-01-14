# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        indexOf = lambda c : ord(c) - ord("a")

        # Firstly ensure strings are of equal length
        if len(word1) != len(word2):
            return False

        # Count letter frequency of each word
        frequencies1 = [0] * 26
        frequencies2 = [0] * 26
        for c1, c2 in zip(word1, word2):
            frequencies1[indexOf(c1)] += 1
            frequencies2[indexOf(c2)] += 1
        
        # Then count the difference of frequencies of letter frequency
        frequencyDifferences = defaultdict(int)
        for freq1, freq2 in zip(frequencies1, frequencies2):
            frequencyDifferences[freq1] += 1
            frequencyDifferences[freq2] -= 1

            # Ensure that the words contain strictly the same characters
            if freq1 == 0 and freq2 > 0:
                return False
        
        # Ensure that the difference of frequencies are 0
        return all(difference == 0 for difference in frequencyDifferences.values())
        

# If we count the letter frequencies of each word, then two strings will be close
# if the set of values in the arrays (independent of index) are equal.

# i.e. these frequency lists are close
# [0, 2, 4, 1, 0, 0] and [0, 1, 2, 4, 0, 0]

# but these are not
# [0, 2, 4, 1, 0, 0] and [2, 1, 1, 0, 3, 0]

# Thus the solution can be obtained by counting the frequencies of the letter
# frequencies of each word and ensuring they are equal.

# We also need to ensure that the words are of equal length and strictly contain
# the same characters.