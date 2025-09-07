# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def sumZero(self, n: int) -> List[int]:
        numbers = []

        # If n is odd, initially add a zero
        if n % 2:
            numbers.append(0)
            n -= 1
        
        # Then, fill the array with positive integers and their complements
        for i in range(1, n // 2 + 1):
            numbers.append(i)
            numbers.append(-i)
        
        # Finally, return the numbers
        return numbers
        