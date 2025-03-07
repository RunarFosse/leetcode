# Author: Runar Fosse
# Time complexity: O(nlog(log(n)))
# Space complexity: O(n)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Using Sieve of Eratosthenes

        # Compute every prime between 1 and right
        sieve = [False] + [True] * (right - 1)
        last_prime, closest_primes = None, [-1, -1]
        for i in range(2, right + 1):
            if not sieve[i - 1]:
                continue
            
            # Store closest primes within range
            if i >= left:
                if last_prime and (closest_primes[0] == -1 or closest_primes[1] - closest_primes[0] > i - last_prime):
                    closest_primes = [last_prime, i]
                
                last_prime = i

            for j in range(i+i, right + 1, i):
                sieve[j - 1] = False
        
        # Return the two closest primes between left and right
        return closest_primes