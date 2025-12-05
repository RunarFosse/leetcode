# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Using prefix sum

        # Keep a running prefix- and suffix sum of the array
        prefix, suffix = 0, sum(nums)

        # Then iterate the array
        partitions = 0
        for num in nums:
            # Update prefix/suffix
            prefix += num
            suffix -= num

            # And count partition if it has an even sum difference
            if suffix and not (suffix - prefix) % 2:
                partitions += 1
        
        # Finally, return the number of those partitions
        return partitions
