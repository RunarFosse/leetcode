# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Using monotonic stack (prefix/suffix min)
        n = len(arr)
        prefix, suffix = [-1] * n, [n] * n
    
        # First calculate index of prefix min
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prefix[i] = stack[-1]
            stack.append(i)

        # Then calculate index of suffix min
        stack = []
        for i in reversed(range(n)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                suffix[i] = stack[-1]
            stack.append(i)

        # Then calculate the final sum
        sum = 0
        for i in range(n):
            sum += arr[i] * ((i - prefix[i]) * (suffix[i] - i))

        return sum % self.mod