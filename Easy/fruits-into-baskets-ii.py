# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Using greedy
        n = len(fruits)
        
        # Iterate the fruits
        unplaced = 0
        for fruit in fruits:
            # Find a fitting basket, and place the fruit
            placed = False
            for i in range(n):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    placed = True
                    break
            
            # If we couldn't place the fruit, count it
            if not placed:
                unplaced += 1

        # Return the count of unplaced fruits
        return unplaced
