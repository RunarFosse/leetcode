# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        digits = len(n)
        palindromes = []
        
        # Add greatest palindromic numbers with one less digit
        palindromes.append(pow(10, digits - 1) - 1)

        # Construct the nearest palindromes with the same number of digits
        leftHalf = int(n[:ceil(digits / 2)])
        palindromes.append(self.palindromize(leftHalf - 1, digits % 2))
        palindromes.append(self.palindromize(leftHalf, digits % 2))
        palindromes.append(self.palindromize(leftHalf + 1, digits % 2))

        # Add smallest palindromic number with one more digit
        palindromes.append(pow(10, digits) + 1)

        # Find the possible palindromic number closest to n
        number, min_distance = int(n), None
        for palindrome in palindromes:
            # If the two numbers are equal, continue
            if number == palindrome:
                continue
            
            # If not, find and store the closest to number
            distance = number - palindrome
            if not min_distance or abs(distance) < abs(min_distance):
                min_distance = distance

        # And return it as a string
        return str(number - min_distance)

    def palindromize(self, num: int, hasOddLength: bool) -> int:
        # Helper function to palindromize first half of a number
        palindrome = num

        # Don't duplicate last digit if number
        # should have odd number of digits
        if hasOddLength:
            num //= 10

        while num:
            palindrome = palindrome * 10 + num % 10
            num //= 10
        return palindrome
        
# When finding the nearest palindromic number there are
# generally three different cases:

# 1. It contains the same number of digits as n
# 2. It contains one more digit than n
# 3. It contains one less digit than n

# The first edge case can be solved be constructing three
# different palindromes from n.
# One which is the left half of n mirrored.
# One which is the left half of n incremented by one mirrored.
# And the last which is the left half of n decremented by one mirrored.

# The second and third edge cases are trivial, as they respectively have to
# be the largest palindromic with one less digit than n (i.e. 10^(n-1) - 1),
# and the smallest palindromic number with one more digit than n
# (i.e. 10^n + 1).

# This leaves us with five possible nearest palindromic numbers, which
# we can brute-forcely compare.