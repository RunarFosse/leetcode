# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        duplicates = []
        for start in range(n):
            # Check where the current number points to
            pointer = abs(nums[start]) - 1

            # If it is positive, it has not been visited
            if nums[pointer] > 0:
                # Visit it by negating it
                nums[pointer] *= -1
            else:
                # If it is visited, the pointer is duplicate
                duplicates.append(pointer+1)
    
        # Return all the duplicates
        return duplicates

# As the elements of the list are on the interval [1, n], we can use
# them as indices pointing to other places in the list. If any points
# to already visited values, they are duplicate.