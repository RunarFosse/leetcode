# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n) 

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        indexOf = lambda c: ord(c) - ord("a")
        universals = []

        # For every word in words2
        frequencies2 = [0] * 26
        for word in words2:
            # Compute the maximum frequency for each character
            frequencies = [0] * 26
            for c in word:
                frequencies[indexOf(c)] += 1
            
            for i in range(26):
                frequencies2[i] = max(frequencies[i], frequencies2[i])
        
        # Then for each word in words1, check if it is universal
        for word in words1:
            frequencies1 = [0] * 26
            for c in word:
                frequencies1[indexOf(c)] += 1
            
            # If it covers the max frequency of every word in words2
            frequencies = zip(frequencies1, frequencies2)
            if all(freq1 >= freq2 for freq1, freq2 in frequencies):
                universals.append(word)
        
        # Finally, return every universal word
        return universals