# Author: Runar Fosse
# Time complexity: O(n + k)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def maxSum(self, nums: List[int], k: int) -> int:
        # Using greedy

        # First, iterate every number
        bits = [0] * 32
        for num in nums:
            # Count every set bit
            index = 0
            while num:
                bit = num & 1
                num >>= 1
                bits[index] += bit
                index += 1
        
        # Then, greedily construct the k largest possible numbers
        total = 0
        for _ in range(k):
            number = 0
            for bit in range(32):
                if bits[bit] > 0:
                    number += (1 << bit)
                    bits[bit] -= 1
            
            # And add their square to the total
            total = (total + number * number) % self.mod
        
        # Finally, return this maximum possible sum of squares
        return total


# Lets say we have to numbers:
# a: 1001111010 (634)
# b: 1100001110 (782)

# Selecting these replaces a with a AND b, and b with a OR b, resulting in:
# a: 1000001010 (522)
# b: 1101111110 (894)

# See how every bit missing from b is moved from a to b. This maximizes b.
# To then find k elements which maximizes their sum of squares, we actually only
# need to count how many of each bit we have, and from these bits construct the
# k largest possible numbers!