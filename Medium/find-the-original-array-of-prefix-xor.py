# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Reverse XOR
        arr = [pref[0] for _ in range(len(pref))]
        for i in reversed(range(1, len(pref))):
            arr[i] = pref[i-1] ^ pref[i]
        
        return arr
        

# The prefix XOR made:
#
# 01001 and 11010 -> 01001 and 10011
# 
# We want to find an operation such that:
#
# 01001 and 10011 -> 01001 and 11010
#
# However, this is just XOR again! Thus the inverse of XOR is XOR.
# Now note, we need to do XOR in reverse order (from the back of pref to front) 
# to correctly invert the operations.