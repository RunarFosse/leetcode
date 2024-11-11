# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Using greedy
        n = len(nums)

        # Precalculate every possible prime smaller than 1000
        primes = self.sieve(1000)
        
        # Iterate the array
        for i in range(n):
            # And subtract the highest possible prime, to make current
            # number strictly larger than last.
            maximum = nums[i] if not i else nums[i] - nums[i-1]
            nums[i] -= primes[bisect_left(primes, maximum)-1]
        
        # Return True if the resulting array is strictly increasing
        return self.isStrictlyIncreasing(nums)
    
    def sieve(self, maximum: int) -> List[int]:
        # Perform Sieve of Eratosthenes algorithm
        isPrime = [True] * maximum
        isPrime[0] = isPrime[1] = False

        primes = [0]
        for i in range(2, maximum):
            if not isPrime[i]:
                continue
            
            primes.append(i)
            for j in range(2, ceil(maximum / i)):
                isPrime[i*j] = False
        
        # Return every prime
        return primes
    
    def isStrictlyIncreasing(self, nums: List[int]) -> bool:
        # Check if nums is a strictly increasing array
        compare = lambda r, e: (r[0] and r[1] < e, e)
        return reduce(compare, nums, (True, 0))[0]


# For every index i, subtract the highest possible
# prime number strictly less than nums[i] and which
# makes nums[i] strictly larger than nums[i-1].

# As any number nums[i] is upper bounded by 1000, the
# Sieve algorithm effectively runs in O(1).