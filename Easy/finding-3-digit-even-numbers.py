# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n!)

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # First, count the frequency of each digit
        frequencies = [0] * 10
        for digit in digits:
            frequencies[digit] += 1
        
        # Then, for each first and second digit
        evens = []
        for first in range(1, 10):
            if frequencies[first] < 1:
                continue
            frequencies[first] -= 1
            for second in range(10):
                if frequencies[second] < 1:
                    continue
                frequencies[second] -= 1

                # Count how many even numbers we can create
                for third in range(0, 10, 2):
                    if frequencies[third] >= 1:
                        evens.append(first * 100 + second * 10 + third)
                
                frequencies[second] += 1
            frequencies[first] += 1
        
        # Finally, return every even 3-digit numbers
        return evens