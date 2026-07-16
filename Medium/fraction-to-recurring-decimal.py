# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # If the numerator is zero, the result is too
        if numerator == 0:
            return "0"
        
        # If either part is negative, but not both
        number = []
        if (numerator < 0) ^ (denominator < 0):
            # Then the result is negative too
            number.append("-")
        
        # Extract the integer part
        dividend = abs(numerator)
        divisor = abs(denominator)
        integer = dividend // divisor
        number.append(str(integer))

        # If the resulting remainder is zero, our number is exact
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(number)
        
        # Otherwise, extract the decimal part too
        seen = {}
        number.append(".")
        while remainder != 0:
            # If we've ever seem this exact remainder before
            if remainder in seen:
                # We have a repeating pattern
                number.insert(seen[remainder], "(")
                number.append(")")
                break
            
            # Otherwise, store current remainder as seen
            seen[remainder] = len(number)

            # And, compute and append the next digits
            remainder *= 10
            digits = remainder // divisor
            number.append(str(digits))
            remainder %= divisor
        
        # Finally, return the resulting number as a string
        return "".join(number)
