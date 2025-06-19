# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # First, sort the array in ascending order
        nums.sort()

        # Then, iterate the array and greedily partition into valid groups
        partitions, minimum = 0, -1e9
        for num in nums:
            # If the difference between the current number and minimum is more than k
            if num - minimum > k:
                # Create a new partition
                partitions += 1
                minimum = num

        # Finally, return the number of partitions
        return partitions
