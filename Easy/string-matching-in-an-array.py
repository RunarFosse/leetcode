# Author: Runar Fosse
# Time complexity: O(m^2n)
# Space complexity: O(m^2n)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Using trie
        class Node():
            def __init__(self):
                self.children = {}
                self.count = 0

        # Iterate every word
        trie = Node()
        for word in words:
            # Add every word substring into the trie
            for i in range(len(word)):
                current = trie
                for j in range(i, len(word)):
                    c = word[j]
                    if c not in current.children:
                        current.children[c] = Node()
                    current = current.children[c]
                    current.count += 1
        
        # Then, iterate every word again, counting matching strings
        matches = []
        for word in words:
            current = trie
            for c in word: 
                current = current.children[c]

            # If the count is higher than one
            if current.count > 1:
                # Then the current word matches at least one more word
                matches.append(word)
        
        # Finally, return all matching words
        return matches
