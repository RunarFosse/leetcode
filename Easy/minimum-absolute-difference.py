# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # First, sort the array in ascending order
        arr.sort()

        # Then, iterate the array
        minimum, pairs = 1e9, []
        for a, b in pairwise(arr):
            # Compute the difference between two adjacent elements
            difference = b - a

            # If this difference is minimal
            if difference <= minimum:
                if difference < minimum:
                    pairs = []
                    minimum = difference
                
                # Then remember the pair
                pairs.append((a, b))
        
        # Finally, return all pairs with minimum absolute difference
        return pairs
