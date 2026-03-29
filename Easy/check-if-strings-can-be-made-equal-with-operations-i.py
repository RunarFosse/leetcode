# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Compute the character frequency difference at even and odd indices
        evens, odds = [0] * 26, [0] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for i in range(4):
            i1, i2 = indexOf(s1[i]), indexOf(s2[i])
            if i % 2:
                odds[i1] += 1
                odds[i2] -= 1
            else:
                evens[i1] += 1
                evens[i2] -= 1
        
        # Then, ensure that all frequencies are zero
        return not any(chain(evens, odds))

        
# This is trivial by computing the character frequency difference at even and odd indices
# If the two strings have no difference in frequency at either even or odd indices,
# then they can be made equal with the operations given.

# With the constraint that both strings are of length 4, we can very easily compute
# whether this is true in constant time and space.