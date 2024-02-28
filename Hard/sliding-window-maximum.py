# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using sliding window
        n = len(nums)

        # First iterate whole first sliding window
        # and store maximums in monotonic stack
        p1, p2 = 0, k-1
        stack = deque([])
        for i in range(p1, p2+1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        
        # Then slide window over array
        max_sliding_window = []
        while p2 < n:
            # Current max is stored in front of monotonic stack
            max_sliding_window.append(stack[0])

            # Move window
            if stack[0] == nums[p1]:
                stack.popleft()
            p1 += 1
            p2 += 1
            if p2 < n:
                while stack and stack[-1] < nums[p2]:
                    stack.pop()
                stack.append(nums[p2])
        
        # Return the maximum sliding window array
        return max_sliding_window