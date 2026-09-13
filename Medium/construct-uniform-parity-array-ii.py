# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Iterate the array
        has_odd, minimum = False, inf
        for num in nums1:
            # Storing if the array contains an odd entry
            has_odd = (num % 2 == 1) or has_odd

            # And the minimum element
            minimum = min(num, minimum)
        
        # Then return if we can make a uniform parity array
        return not has_odd or (minimum % 2 == 1)


# If all elements already are all odd or all even, the array already has uniform parity.

# However, if not, then the only way for the array to become uniform parity is if
# the smallest element is an odd number. In this way, all other elements can
# also be turned odd.

# To trivialize this problem, it can thus be transformed into a uniform parity array if
# and only if there are no odd elements in the array, or if the smallest element is odd.