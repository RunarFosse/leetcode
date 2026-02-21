# Author: Runar Fosse
# Time complexity: O(n + log(n)log(log(log(n))))
# Space complexity: O(log(n))

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Using Sieve of Eratosthenes

        # Compute the number of (both set and unset) bits in right
        total_bits = ceil(log2(right))

        # Compute every prime from 1 up to the number of bits in right
        sieve = [False] + [True] * total_bits
        for bits in range(2, total_bits + 1):
            if not sieve[bits - 1]:
                continue

            for number in range(bits + bits, total_bits + 1, bits):
                sieve[number - 1] = False
        
        # Then, iterate every number between left and right
        prime_bits = 0
        for number in range(left, right + 1):
            # Counting every number with a prime number of bits
            if sieve[number.bit_count() - 1]:
                prime_bits += 1

        # Finally, return this count
        return prime_bits
