# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Store a set containing only values with a frequency of 1
        uniques = set()
        for num in nums:
            # Add if not in uniques
            if num not in uniques:
                uniques.add(num)
            # Remove if in uniques
            else:
                uniques.remove(num)
        
        # Return remaining elements
        return list(uniques)
