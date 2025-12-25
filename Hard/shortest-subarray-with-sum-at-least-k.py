# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Maintain a prefix sum, as well as monotonic queue with previous prefix sums
        prefix, queue = 0, deque([])

        # Then iterate the array, computing shortest subarray
        subarray = 1e9
        for end in range(n):
            # If current prefix value is larger than k, store possible subarray size
            prefix += nums[end]
            if prefix >= k:
                subarray = min(end + 1, subarray)

            # If we can prune elements, and preserve a value of at least k, then do so
            while queue and prefix - queue[0][0] >= k:
                _, start = queue.popleft()
                subarray = min(end - start, subarray)
            
            # And maintain a strictly decreasing monotonic queue
            while queue and queue[-1][0] > prefix:
                queue.pop()
            queue.append((prefix, end))
        
        # Finally, return shortest subarray with sum of at least k, if it exists
        return subarray if subarray < 1e9 else -1
