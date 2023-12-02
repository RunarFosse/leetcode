# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # First count occurences in chars
        valid_occurences = defaultdict(lambda: 0)
        for char in chars:
            valid_occurences[char] += 1
        
        # Then for each word, count occurences and verify it is valid
        lengths = 0
        for word in words:
            occurences = defaultdict(lambda: 0)
            valid = True
            for char in word:
                occurences[char] += 1
                if occurences[char] > valid_occurences[char]:
                    valid = False
                    break

            if valid:
                lengths += len(word)
        
        return lengths