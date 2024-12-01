# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Store every number seen in a set
        seen = set()

        for num in arr:
            # Check if half or double the current number has been seen
            if num / 2 in seen or num * 2 in seen:
                return True
            
            seen.add(num)
        
        # If not, no pair with N and its double exists
        return False