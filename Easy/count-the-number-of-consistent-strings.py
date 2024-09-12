# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # First turn the allowed letters into an array,
        # where the value is true for every character which is allowed
        isAllowed = [False] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for c in allowed:
            isAllowed[indexOf(c)] = True
        
        # Then iterate every word, ensuring that every character is allowed
        consistents = 0
        for word in words:
            isConsistent = all(map(lambda c: isAllowed[indexOf(c)], word))
            if isConsistent:
                consistents += 1
        
        # Return every consistent word
        return consistents

# As every word can be at most of length 10, we imply the inner for loop
# runs in constant time (at most 10 iterations).