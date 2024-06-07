# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Using prefix tree

        # First generate a prefix tree (trie) out of the dictionary
        class Node():
            def __init__(self):
                self.children = {}
                self.end = False
        trie = Node()
        for word in dictionary:
            current = trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.end = True
        
        # Then iterate sentence, replacing derivatives with their roots
        words = []
        for word in sentence.split(" "):
            current = trie
            result = []
            # For each word
            for i in range(len(word)):
                c = word[i]
                # Check if in the prefix tree
                if c in current.children:
                    current = current.children[c]
                    result.append(c)
                    # If we are at the end of a word (root), stop iterating
                    if current.end:
                        break
                # If word is not in the prefix tree, add the whole word
                else:
                    result += word[i:]
                    break
            words.append("".join(result))
        
        # Return the resulting string of words
        return " ".join(words)