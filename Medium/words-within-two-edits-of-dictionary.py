# Author: Runar Fosse
# Time complexity: O(mk + nk^3)
# Space complexity: O(mk)

# with k being the maximum length of a word

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Using trie
        class Node():
            def __init__(self):
                self.children = {}
                self.terminates = False
        
        # Add every word in the dictionary to a trie
        trie = Node()
        for word in dictionary:
            current = trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.terminates = True
        
        # Then, iterate every query
        words = []
        for query in queries:
            # Perform DFS on the trie
            queue = [(0, 2, trie)]
            while queue:
                i, edits, current = queue.pop()
                
                # If we have a valid word within two edits
                if i == len(query):
                    if current.terminates:
                        # Add to words and break DFS
                        words.append(query)
                        break
                    continue
                
                # Iterate all the characters from the current trie node
                for c, child in current.children.items():
                    if c == query[i]:
                        queue.append((i + 1, edits, child))
                        continue
                    
                    # If we have an available edit, modify the current character
                    if edits:
                        queue.append((i + 1, edits - 1, child))
        
        # Finally, return the query words with a dictionary word within maximum two edits
        return words
