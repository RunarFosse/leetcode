# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # Compute the character frequency difference at even and odd indices
        evens, odds = [0] * 26, [0] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for i in range(n):
            i1, i2 = indexOf(s1[i]), indexOf(s2[i])
            if i % 2:
                odds[i1] += 1
                odds[i2] -= 1
            else:
                evens[i1] += 1
                evens[i2] -= 1
        
        # Then, ensure that all frequencies are zero
        return not any(chain(evens, odds))
