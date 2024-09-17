# Author: Runar Fosse
# Time complexity: O(m+n)
# Space complexity: O(m+n)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Iterate every word in both sentences
        frequency = defaultdict(int)
        for word in s1.split(" ") + s2.split(" "):
            # Store frequency of each word
            frequency[word] += 1
        
        # Return every word appearing exactly once over both sentences
        return filter(lambda word: frequency[word] == 1 , frequency.keys())
