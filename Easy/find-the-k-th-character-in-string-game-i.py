# Author: Runar Fosse
# Time complexity: O(log k)
# Space complexity: O(1)

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Using binary search

        # While we can't accurately represent the k'th character
        offset = 0
        while k > 1:
            # Compute the largest bit in k
            largest_bit = k.bit_length() - 1

            # It k is a pure multiple of 2
            if (1 << largest_bit) == k:
                # Subtract the following bit instead
                largest_bit -= 1
            
            # Subtract from k, and increment the character
            k -= (1 << largest_bit)
            offset = (offset + 1) % 26

        # Finally, return the k'th character
        return chr(offset + ord("a"))
        