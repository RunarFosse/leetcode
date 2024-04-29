# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Using bit manipulation

        # Calculate XOR over array
        xor = reduce(lambda a, b: a ^ b, nums)

        # Return the number of bits which differ between xor and k
        return (xor ^ k).bit_count()