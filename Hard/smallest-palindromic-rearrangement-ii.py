# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Using combinatorics
        n = len(s)

        # First, compute half the frequency of each character
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for i in range(n // 2):
            frequencies[indexOf(s[i])] += 1
        
        # If the string has odd length, extract the middle character
        middle = s[n // 2] if n % 2 else ""

        # Then, compute the number of permutations without exceeding memory
        permutations, prefix = 1, 0
        for frequency in frequencies:
            permutations = permutations * self.choose((n >> 1) - prefix, frequency)
            prefix += frequency
        
        # If there are less than k possible distinct permutations
        if k > permutations:
            # Return the empty string
            return ""
        
        # Otherwise, compute the smallest palindromic string
        first, smallest, remaining = [], 0, (n // 2)
        for _ in range(n // 2):
            # Move the pointer up to the lexicographically smallest available character
            while frequencies[smallest] == 0:
                smallest += 1

            # For every candidate character for this position
            p = permutations
            for i in range(smallest, 26):
                if frequencies[i] == 0:
                    continue

                # Compute the number of permutations after this character
                p = (permutations * frequencies[i]) // remaining
            
                # If k is less than or equal to the number of next permutations
                if k <= p:
                    # This is in position for the k'th palindromic rearrangement
                    first.append(chr(i + ord("a")))

                    # Then decrement the remaining permutation count
                    permutations = (permutations * frequencies[i]) // remaining
                    frequencies[i] -= 1
                    remaining -= 1
                    break

                # Otherwise, remove these permutations from the current
                k -= p

        # Finally, return the k-th lexicographically smallest palindromic permutation
        return "".join(first + [middle] + first[::-1])
    
    def choose(self, a: int, b: int) -> int:
        # Compute the binomial coefficient a choose b
        return self.factorial(a) // (self.factorial(b) * self.factorial(a - b))
    
    @functools.cache
    def factorial(self, num: int) -> int:
        # Compute the factorial of num
        if num <= 1:
            return 1
        return num * self.factorial(num - 1)


# Given a string with a 'a's, b 'b's, c 'c's, ..., z 'z's. Then the number of 
# palindromic strings we can create is:
# Given f1 = a // 2, f2 = b // 2, f3 = c // 2, ..., f26 = z // 2
# (f1 + f2 + f3 + ... + f26)! / (f1! * f2! * f3! * ... * f26!).

# To find the k'th permutation, iterate each character one by one.
# Compute how many permutations 0 using only the other remaining characters exist.
# If we are looking at a, then:
# p = ((f1 - 1) + f2 + f3 + ... + f26)! / ((f1 - 1)! * f2! * f3! * ... * f26!)

# The next p can also be bootstrapped from current p using for each character i:
# p_i = p * f_i / n,          where n is the remaining number of characters.

# We can also efficiently compute the initial p, using:
# p_n = p_(n-f_i) * ((n - sum(f_i' for all i' < i)) choose f_i)
#     = p_(n-f_i) * (n - f1 - f2 - .. - f_(i-1))! / (f_i! * (n - f1 - f2 - .. - f_i)!)

# If k <= p, then we know that the k'th permutation starts with this character (a).
# Thus, add 'a' to string, decrement f1, and continue from the current smallest,
# non-zero frequency character.

# Otherwise, k > p, then the permutation does not start with this character (a).
# Jump over all permutations p, by setting k -= p, and continue from the next character.

# Assuming precomputed factorials, 
# the time complexity of this solution is O(n / 2 * 26) = O(n).