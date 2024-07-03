# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If there are smaller than 5 numbers in the list,
        # we always result with a difference of 0 after 3 moves
        if len(nums) < 5:
            return 0

        # Compute the 4 smallest and largest entries within nums
        smallest = nsmallest(4, nums)
        largest = nlargest(4, nums)
        
        # Compute the 4 possible differences and return the smallest
        return min(largest[i]-smallest[3-i] for i in range(4))

# As we are supposed to minimize the difference between the largest 
# and smallest element in the array, we should only change (equivalent
# to remove) either of the three smallest or largest elements in the array.

# The answer can easily be calculated by computing the four different
# differences we could end up with after three moves, and selecting the
# smaller one. Those four differences are:
# 1st Largest - 4th Smallest
# 2nd Largest - 3rd Smallest
# 3rd Largest - 2nd Smallest
# 4th Largest - 1st Smallest

# Calculating these can be done in O(n) time by extracting from heap
# using nsmallest/nlargest. These have a time complexity of O(nlog k),
# where k is the total number of extracted elements. In this case, k = 4,
# such that this in total is a O(n) operation.
# Heap is create in-place, leading to this having a space complexity of O(1).