# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n, m = len(sentence), len(searchWord)

        # Keep track of the current letter in the searchWord and sentence
        searchIndex, sentenceIndex = 0, 0

        # Then iterate the sentence string
        wordIndex = 1
        while sentenceIndex < n:
            # Iterate every word
            while sentenceIndex < n and sentence[sentenceIndex] != " ":
                # If searchWord is not a prefix, break
                if searchWord[searchIndex] != sentence[sentenceIndex]:
                    break
                
                # However if we have, continue iterating
                searchIndex += 1
                sentenceIndex += 1

                # If we've fully iterated the searchWord, it is a prefix
                if searchIndex == m:
                    return wordIndex
            
            # Move onto the next word
            wordIndex += 1
            searchIndex = 0
            while sentenceIndex < n and sentence[sentenceIndex] != " ":
                sentenceIndex += 1
            sentenceIndex += 1
        
        # If loop terminates, the searchWord isn't a prefix of any word
        return -1