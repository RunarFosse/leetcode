# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Declare some helper functions
        indexOf = lambda c: ord(c) - ord("a")
        weightOf = lambda c: weights[indexOf(c)]
        characterOf = lambda i: chr(ord("z") - i)

        # Then iterate every word
        result = []
        for word in words:
            # Compute the weight of the word
            weight = sum(map(weightOf, word))

            # And store the reverse alphabetical mapping in the result
            result.append(characterOf(weight % 26))
        
        # Finally, return the resulting string
        return "".join(result)
