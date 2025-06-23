# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # Using greedy

        # For every base 10 palindrome
        mirrors, palindromes = 0, self.base10Palindromes()
        while n:
            # If the current palindrome is a k-mirror
            current = next(palindromes)
            if self.isMirror(current, k):
                # Add it to the sum
                mirrors += current
                n -= 1
        
        # Finally, return the sum of n k-mirror numbers
        return mirrors
        
    def base10Palindromes(self) -> Generator[int, None, None]:
        # Build all base 10 palindromes in order
        digits = 1
        while True:
            # Compute the current left start and end bounds
            length = (digits + 1) // 2
            start = pow(10, length - 1)
            end = pow(10, length)

            # For every left piece of the number, compute and yield palindrome
            for half in range(start, end):
                left = str(half)
                if digits % 2 == 0:
                    yield int(left + left[::-1])
                else:
                    yield int(left + left[:-1][::-1])
            
            # Increment the digit count
            digits += 1

    def isMirror(self, num: int, base: int) -> bool:
        # Turn the number into its respective base
        digits = []
        while num:
            num, digit = divmod(num, base)
            digits.append(digit)
        
        # And check if it is a mirror number
        return digits == digits[::-1]