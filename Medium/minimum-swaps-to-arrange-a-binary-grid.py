# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Using greedy
        n = len(grid)
        
        # First, iterate each row
        rightmost = []
        for i in range(n):
            # Finding the position of the rightmost 1
            position = 0
            for j in reversed(range(n)):
                if grid[i][j]:
                    position = j
                    break
            rightmost.append(position)
        
        # Then, iterate each row again
        swaps = 0
        for i in range(n):
            # If row already makes grid binary, continue
            if rightmost[i] <= i:
                continue

            # Otherwise, find the first row which makes grid binary
            index = i + 1
            while index < n and rightmost[index] > i:
                index += 1
            
            # If there are no index making grid binary, it is impossible
            if index == n:
                return -1
            
            # And swapping it
            rightmost.insert(i, rightmost.pop(index))
            swaps += index - i
        
        # Finally, return the number of swaps
        return swaps
