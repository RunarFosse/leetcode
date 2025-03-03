# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Create three arrays to hold smaller, equal and larger than pivot
        smaller, equal, larger = [], [], []

        # Iterate the array, binning each element respectively
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        
        # Finally, return the union of the arrays
        return smaller + equal + larger