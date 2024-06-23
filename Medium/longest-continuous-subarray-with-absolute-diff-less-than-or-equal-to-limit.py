# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Using sliding window
        n = len(nums)

        # Store mins and maxes in monotonic queue
        mins, maxs = deque([]), deque([])

        longest = 0
        start = -1
        for end in range(n):
            # Update monotonic queue to include new element
            while mins and mins[-1][1] > nums[end]:
                mins.pop()
            mins.append((end, nums[end]))
            while maxs and maxs[-1][1] < nums[end]:
                maxs.pop()
            maxs.append((end, nums[end]))

            # Check if subarray is invalid, reshape
            while abs(maxs[0][1] - mins[0][1]) > limit:
                # Reshaping is done by popping first occuring
                # element and moving start pointer to its index
                if maxs[0][0] < mins[0][0]:
                    start = maxs.popleft()[0]
                else:
                    start = mins.popleft()[0]
            
            # Then store current subarray length if longest
            longest = max(end - start, longest)

        return longest
