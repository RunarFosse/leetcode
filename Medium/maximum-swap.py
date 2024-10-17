# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def maximumSwap(self, num: int) -> int:
        # First compute suffix max of digits
        suffixes = []
        digits = []

        i = 0
        while num:
            digit = num % 10
            digits.append(digit)

            suffix = (digit, i)
            if suffixes and suffixes[-1][0] >= digit:
                suffix = suffixes[-1]

            suffixes.append(suffix)

            num //= 10
            i += 1
        
        # Then iterate number, replacing the first occuring digit
        # with a larger suffix
        replace = None
        while digits:
            num *= 10
            i -= 1

            digit = digits.pop()
            suffix = suffixes.pop()

            if not replace and digit < suffix[0]:
                num += suffixes[-1][0]
                replace = (digit, suffix[1])
            elif replace and i == replace[1]:
                num += replace[0]
            else:
                num += digit
        
        # Finally return the number
        return num
        
# We always want to swap the first occuring digit with a higher digit
# occuring later in the number. If several of this higher digit appear, we
# swap with the last one.