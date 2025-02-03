# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Using trie
        class Node():
            def __init__(self):
                self.children = {}
                self.index = None
                self.score = 0
        
        # Iterate the words array
        prefix, suffix = Node(), Node()
        count = 0
        for i, word in enumerate(words):
            # Count prefix and suffix pairs
            current, reverse = prefix, suffix
            for c1, c2 in zip(word, reversed(word)):
                if c1 not in current.children or c2 not in reverse.children:
                    break
                current = current.children[c1]
                reverse = reverse.children[c2]
                if current.index == reverse.index:
                    count += current.score

            # Then, add word to tries
            current, reverse = prefix, suffix
            for c1, c2 in zip(word, reversed(word)):
                if c1 not in current.children:
                    current.children[c1] = Node()
                current = current.children[c1]
                if c2 not in reverse.children:
                    reverse.children[c2] = Node()
                reverse = reverse.children[c2]
            current.score += 1
            reverse.score += 1
            current.index = reverse.index = i
    
        # Finally, return the count of all prefix and suffix pairs
        return count