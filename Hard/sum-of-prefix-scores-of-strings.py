# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Using trie
        class Node():
            def __init__(self):
                self.children = {}
                self.score = 0

        # For each word in the list of words,
        # build, traverse and increment nodes in prefix trie
        trie = Node()
        for word in words:
            current = trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
                current.score += 1

        # Then again, for each word, traverse the trie,
        # counting cumulative score on its path
        scores = []
        for word in words:
            current, score = trie, 0
            for c in word:
                current = current.children[c]
                score += current.score
            scores.append(score)
        
        # Return the list of scores
        return scores