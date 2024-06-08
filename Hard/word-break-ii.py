# Author: Runar Fosse
# Time complexity: O(n2^n)
# Space complexity: O(n2^n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Using dynamic programming
        self.s, self.n = s, len(s)

        # First generate a prefix tree out of the dictionary
        class Node():
            def __init__(self):
                self.children = {}
                self.end = False
        self.trie = Node()
        for word in wordDict:
            current = self.trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.end = True
        
        # Then perform dynamic programming
        return self.opt(0)
    
    @functools.cache
    def opt(self, i: int) -> List[str]:
        if i == self.n:
            return [""]
        
        # First we iterate string to find all valid possible starting words
        words = []
        node, word = self.trie, []
        for j in range(i, self.n):
            c = self.s[j]
            if c in node.children:
                word.append(c)
                node = node.children[c]
            else:
                break
            if node.end:
                words.append(("".join(word), j))
        
        # Then iterate them and combine with later valid strings
        valids = []
        for word, j in words:
            later_valids = self.opt(j+1)
            for string in later_valids:
                valids.append(word + (" " if string else "") + string)
        
        # Return all valid strings which can be created
        return valids
        

# opt(i) - All valid possible sentences that can be created starting
#          from index i

# Base case:
# opt(n) = [""]

# Recurrency:
# opt(i) = concat([word + next_words for next_words in opt(j+1) if next_words
#                              for (all valid) word in s[i:j+1]])
# opt(i) = [] if there are no valid words starting at index i
