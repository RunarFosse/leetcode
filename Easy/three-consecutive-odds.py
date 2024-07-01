# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Iterate the array
        consecutive = 0
        for num in arr:
            # If a number is odd, increment consecutive count, reset if not
            if num % 2:
                consecutive += 1
            else:
                consecutive = 0
            
            # If there has been three consecutive odds, return True
            if consecutive == 3:
                return True
        
        # If for loop terminates, there does not exist three consecutive odds
        return False