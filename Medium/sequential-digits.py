# Author: Runar Fosse
# Time complexity: O(log(m/n)*log(m))
# Space complexity: O(log(m/n))

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = []

        # Extract initial logarithm and multiplier from the lower bound
        logarithm = floor(log10(low))
        multiplier = low // pow(10, logarithm)
        if multiplier + logarithm > 9:
            logarithm += 1
            multiplier = 1
        number = self.constructSequential(logarithm, multiplier)

        # While the constructed sequential digit number is within bounds
        while number <= high:
            # Add to list
            if number >= low:
                numbers.append(number)

            # And increment multiplier/logarithm
            multiplier += 1
            if multiplier + logarithm > 9:
                logarithm += 1
                multiplier = 1
            
            # If logarithm is higher than 8, we have to break prematurely
            if logarithm > 8:
                break
            
            number = self.constructSequential(logarithm, multiplier)
        
        # Return the constructed sequential digits
        return numbers
        
    def constructSequential(self, logarithm: int, multiplier: int) -> int:
        number = multiplier
        # Iterate through the number, adding contiguously increasing digits
        while logarithm:
            multiplier += 1
            number = number * 10 + multiplier
            logarithm -= 1
        return number

# We can construct all different sequential digit number between low and high.
# As all sequential digit numbers follow inferrable rules, this will be trivial.