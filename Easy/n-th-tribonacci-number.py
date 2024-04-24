# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        # Using sliding window

        # Early break if basecase
        if n in [0, 1, 2]:
            return 0 if not n else 1

        # Iteratively calculate specific tribonacci number
        current = 1
        window = deque([0, 0, 1, 1])
        for _ in range(3, n+1):
            # Calculate current tribonacci
            current *= 2

            # Remove front of window
            current -= window.popleft()

            # Append current to window
            window.append(current) 
        
        # Return N-th tribonacci number
        return current