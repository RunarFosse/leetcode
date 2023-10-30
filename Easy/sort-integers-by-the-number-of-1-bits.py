# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Define a sort function sorting by bit count
        # (This first sorts by bit_count(), then int value)
        
        arr.sort(key=lambda i : (i.bit_count(), i))
        return arr

# int.bit_count() has time complexity of O(log k)
# Now, as every number i <= 10^4, then log_2(10^4) ≈ 13, time is negligible
# i.e. we treat it as O(1)