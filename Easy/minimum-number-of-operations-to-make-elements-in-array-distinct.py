# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate the array from the back
        seen = set()
        for i in reversed(range(n)):
            # If we've seen an element before, it is a duplicate
            if nums[i] in seen:
                # Return minimum number of operations
                operations, remaining = divmod(i, 3)
                if remaining < 3:
                    operations += 1
                return operations

            # Otherwise, mark element as seen
            seen.add(nums[i])
        
        # If loop terminates, it is already distinct
        return 0