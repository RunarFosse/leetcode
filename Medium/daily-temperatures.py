# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Using monotonic stack
        n = len(temperatures)
        answer = [0] * n

        stack = []
        # Iterate temperatures list from behind
        for i in reversed(range(len(temperatures))):
            # While the stored top value in the stack has a lower (or equal)
            # temperature than the current day, pop it from the top
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            # Find closest day which is warmer from the stack
            answer[i] = (stack[-1][1] - i) if stack else 0
            
            # Add the current day's temperature to the stack
            stack.append((temperatures[i], i))
        
        # Return the answer list
        return answer