# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Using min heap
        n = len(nums)

        # Create a linked list to efficiently handle element consolidation
        left, right = [None] * n, [None] * n

        # Create a min heap storing pairs with the minimum sum
        heap = []

        # Then iterate the array in pairs
        inversions = 0
        for i, j in pairwise(range(n)):
            # Populate the linked list
            left[j] = i
            right[i] = j

            # Add pair with sum to heap
            heappush(heap, (nums[i] + nums[j], i, j))

            # Count inversions
            if nums[i] > nums[j]:
                inversions += 1
        
        # Then count number of operations to remove all inversions
        operations = 0
        while inversions:
            # Grab the pair with the minimum sum
            sum, i, j = heappop(heap)

            # If this pair is stale, continue
            if right[i] != j or left[j] != i or nums[i] + nums[j] != sum:
                continue

            # Otherwise, decrement possible inversions
            if left[i] is not None and nums[left[i]] > nums[i]:
                inversions -= 1
            if nums[i] > nums[j]:
                inversions -= 1
            if right[j] is not None and nums[j] > nums[right[j]]:
                inversions -= 1
            
            # Replace pair with their sum, and update linked list
            nums[i] = sum
            right[i] = right[j]
            if right[i] is not None:
                left[right[i]] = i

            # And increment possible inversions again
            if left[i] is not None and nums[left[i]] > nums[i]:
                inversions += 1
            if right[i] is not None and nums[i] > nums[right[i]]:
                inversions += 1
            
            # Finally, increment operations count and add pairs back to heap
            operations += 1
            if left[i] is not None:
                heappush(heap, (nums[left[i]] + nums[i], left[i], i))
            if right[i] is not None:
                heappush(heap, (nums[i] + nums[right[i]], i, right[i]))
        
        # Finally, return the minimum number of operations to make array non-decreasing
        return operations
