# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(1)

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        m = len(pref)
        
        # Count the number of words with pref as a prefix
        count = 0
        for word in words:
            # If the word is smaller than pref, then it cannot be a prefix
            if len(word) < m:
                continue
            
            # If not, add if word has pref as prefix
            if all(word[i] == pref[i] for i in range(m)):
                count += 1
        
        # Return the count of all words with prefix
        return count