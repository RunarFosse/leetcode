# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # Using prefix sum
        n = len(nums)

        # Compute prefix maximums and suffix minimums of the array
        prefixes, suffixes = [nums[0]], [nums[n - 1]]
        for i in range(1, n):
            prefixes.append(max(nums[i], prefixes[-1]))
            suffixes.append(min(nums[n - 1 - i], suffixes[-1]))
        
        # Then, compute the answer from behind
        maximums = [0] * n
        maximums[n - 1] = prefixes[n - 1]
        for i in reversed(range(n - 1)):
            # If the maximum prefix is smaller or equal to the minimum suffix
            if prefixes[i] <= suffixes[n - 1 - (i + 1)]:
                # Then we have a cut, meaning no jump can cross
                maximums[i] = prefixes[i]
            else:
                # Otherwise, we can jump our element on the right
                maximums[i] = maximums[i + 1]
        
        # Finally, return all the maximum values reachable from every index
        return maximums


# Because we can jump to any element to the right that is lower, and any element
# to the left that is higher, then transitively, all elements are connected to eachother
# unless we have an index k in which all elements to the left of k are either
# equal to or less than every element to the right of k.

# By finding all these cutting indices k we can trivially solve the problem, as each
# interval partitioned by these k's have the same answer, that being their maximum entry.