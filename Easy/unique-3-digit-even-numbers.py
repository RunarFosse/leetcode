# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # First, count the frequency of each digit
        frequencies = [0] * 10
        for digit in digits:
            frequencies[digit] += 1
        
        # Then, iterate all possible 3-digit even numbers (without leading zeros)
        uniques = 0
        for i in range(1, 10):
            if frequencies[i] == 0:
                continue
            frequencies[i] -= 1

            for j in range(10):
                if frequencies[j] == 0:
                    continue
                frequencies[j] -= 1

                for k in range(0, 10, 2):
                    if frequencies[k] == 0:
                        continue

                    # If we have enough of all digits, we can create this number
                    uniques += 1

                frequencies[j] += 1
            frequencies[i] += 1
        
        # Finally, return the number of unique 3-digit even numbers we can create
        return uniques
