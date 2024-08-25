# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Turn the expression into a generator,
        # extracting each new fraction one by one
        expression = self.iterate(expression)

        # Then iterate every fraction
        numerator, denominator = next(expression)
        for next_numerator, next_denominator in expression:
            # Find the least common multiple between the two denominators
            multiple = lcm(denominator, next_denominator)

            # Turn both fractions into a common multiple by multiplying
            # with the other factor of the least common multiple
            numerator *= multiple // denominator
            next_numerator *= multiple // next_denominator

            # Add them together
            numerator += next_numerator
            denominator = multiple

            # Then reduce our fraction by finding the greatest common divisor
            divisor = gcd(numerator, denominator)
            numerator //= divisor
            denominator //= divisor
        
        # Finally, return the resulting fraction as a string
        return str(numerator) + "/" + str(denominator)
    
    def iterate(self, expression: str) -> Iterator[Tuple[int, int]]:
        pointer, n = 0, len(expression)
        while pointer < n:
            # Check if next fraction should be negative
            negative = expression[pointer] == "-"
            if not expression[pointer].isnumeric():
                pointer += 1
            
            # Extract numerator and denominator from expression
            numerator, denominator = None, None
            while pointer < n and expression[pointer].isnumeric():
                digit = int(expression[pointer])
                numerator = digit if not numerator else numerator * 10 + digit
                pointer += 1
            pointer += 1
            while pointer < n and expression[pointer].isnumeric():
                digit = int(expression[pointer])
                denominator = digit if not denominator else denominator * 10 + digit
                pointer += 1
            
            # Turn numerator negative if needed, before returning
            if negative:
                numerator *= -1
            
            yield numerator, denominator
