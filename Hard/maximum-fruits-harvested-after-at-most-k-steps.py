# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Using sliding window
        n = len(fruits)

        # Slide a window over the array, counting fruits within
        maximum = 0
        left, right, harvested = 0, 0, 0
        while right < n:
            # Count the current harvest
            harvested += fruits[right][1]

            # Shrink the window if we cannot reach it
            while left <= right and self.steps(left, right, fruits, startPos) > k:
                harvested -= fruits[left][1]
                left += 1
            
            # And store the maximum number of harvested fruits
            maximum = max(harvested, maximum)

            # And widen the window
            right += 1
        
        # Finally, return this maximum possible harvested fruits
        return maximum
    
    def steps(self, left: int, right: int, fruits: List[int], startPos: int) -> int:
        # Compute the minimum number of steps it takes to cover the window
        leftPos, rightPos = fruits[left][0], fruits[right][0]
        initial = min(abs(leftPos - startPos), abs(rightPos - startPos)) 
        return initial + (rightPos - leftPos)
        