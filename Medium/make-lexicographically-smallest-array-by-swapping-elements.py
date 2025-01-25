# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Store subsequences, and which subsequence each number exists in
        subsequences, indices = [deque([])], {}

        # Sort and iterate the sorted array
        n, ascending = len(nums), sorted(nums)
        for i in range(n):
            # Add number to current subsequence
            number, index = ascending[i], len(subsequences) - 1
            subsequences[index].append(number)
            indices[number] = index

            # If the next number is outside the limit, add another subsequence
            if i < n - 1 and abs(number - ascending[i + 1]) > limit:
                subsequences.append(deque([]))

        # Finally, iterate the unsorted array and "sort" subsequences
        for i in range(n):
            # Find the subsequence of the current number
            number = nums[i]
            index = indices[number]

            # And replace it with the smallest yet number from the subsequence
            nums[i] = subsequences[index].popleft()
        
        # Finally, return the array
        return nums

# Thorugh the array, a subsequence will end up in sorted order if and only if
# every element in that subsequence has at least one other element within the
# limit, also in the subsequence.

# Therefore we only need to find every such subsequence, and rearrange them
# such that they end up sorted.