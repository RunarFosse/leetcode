# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Using trie

        # Generate a suffix trie from the given words
        trie = Node(0)
        for i, word in enumerate(wordsContainer):
            # By iterating the word in reverse order and constructing trie
            current = trie
            for c in reversed(word):
                # Storing the shortest child word with the given suffix
                if len(word) < len(wordsContainer[current.shortest]):
                    current.shortest = i

                if c not in current.children:
                    current.children[c] = Node(i)
                current = current.children[c]

            if len(word) < len(wordsContainer[current.shortest]):
                current.shortest = i
        
        # Then, iterate the queries
        results = []
        for query in wordsQuery:
            # Find the word in trie with the longest common suffix to query
            current = trie
            for c in reversed(query):
                # If there are no words that match suffix, stop traversal
                if c not in current.children:
                    break
                
                # Otherwise, continue down the trie
                current = current.children[c]
            
            # And return the current smallest word matching prior suffix
            results.append(current.shortest)

        # Finally, return the result of the queries
        return results

class Node():
    def __init__(self, index: int):
        self.children = {}
        self.shortest = index
