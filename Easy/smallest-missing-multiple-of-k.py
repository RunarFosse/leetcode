# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Iterate all the numbers
        bitset = 0
        for num in nums:
            # Storing seen multiples of k in a bitset
            multiplier, remainder = divmod(num, k)
            if not remainder:
                bitset |= (1 << (multiplier - 1))
        
        # Extract the rightmost unset bit
        bit = bitset ^ (bitset | (bitset + 1))
        
        # This bit denotes our smallest positive multiplier of k missing
        multiplier = bit.bit_length()

        # Thus, return this multiple of k
        return multiplier * k
