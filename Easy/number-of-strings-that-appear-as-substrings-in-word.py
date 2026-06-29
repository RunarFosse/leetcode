# Author: Runar Fosse
# Time complexity: O(mk + nk)
# Space complexity: O(mk)

# where k is the length of the longest string pattern

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Using trie
        n = len(word)

        class Node():
            def __init__(self):
                self.children = {}
                self.count = 0

        # First, create a trie and populate with the patterns
        trie = Node()
        for pattern in patterns:
            current = trie
            for c in pattern:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.count += 1
        
        # Then, iterate every character in the word
        strings = 0
        for i in range(n):
            # Then, count how many patterns start from this index
            current, j = trie, i
            while j < n and word[j] in current.children:
                current = current.children[word[j]]
                j += 1
                
                # If we have a pattern, count them and remove
                if current.count:
                    strings += current.count
                    current.count = 0

        # Finally, return the total number of strings that appear as substrings
        return strings
