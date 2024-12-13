# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Using monotonic stacks
        score, stack = 0, []
        for num in nums:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                while stack:
                    score += stack.pop()
                    if stack:
                        stack.pop()
        
        # Finally pop the remaining values of the stack
        while stack:
            score += stack.pop()
            if stack:
                stack.pop()
        
        # Return the final score
        return score
            


# We have that an element will always be chosen if it is smaller than both its
# neighbours. Therefore we have an efficient solution using monotonic stacks.