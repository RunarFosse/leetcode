# Author: Runar Fosse
# Time complexity: O((log n)^2)
# Space complexity: O(log n)

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Using trie
        self.n = n

        # Start from the first number
        number = 1
        k -= 1

        # Iterate the trie until we find the target number
        while k:
            # Calculate the size of the current subtrie, rooted in number
            subtrieSize = self.calculateSubtrieSize(number, number+1)

            # If the subtrie is bigger than k, target number is within
            if subtrieSize > k:
                number *= 10
                k -= 1
            
            # If not, target number is in another subtrie
            else:
                number += 1
                k -= subtrieSize

        # Finally, return the target number
        return number
    
    def calculateSubtrieSize(self, number: int, comparator: int) -> int:
        if number > self.n:
            return 0

        # Calculate the number of valid nodes on the current layer
        currentSize = min(comparator, self.n+1) - number

        # As well as the number of nodes on the remaining subtrie
        remainingSize = self.calculateSubtrieSize(number*10, comparator*10)

        # And return the sum
        return currentSize + remainingSize