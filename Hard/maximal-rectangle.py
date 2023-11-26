# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(m)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Using stack
        n, m = len(matrix), len(matrix[0])

        max_rectangle = 0
        cumulative_row = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                # Cumulate new row
                if matrix[i][j] == "0":
                    cumulative_row[j] = 0
                else:
                    cumulative_row[j] += 1
            
            # Perform Largest Rectangle algorithm
            max_rectangle = max(self.largestRectangleArea(cumulative_row), max_rectangle)

        return max_rectangle

    # Directly copied from "https://leetcode.com/problems/largest-rectangle-in-histogram/"
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Using stack
        n, maxarea = len(heights), 0

        stack = []
        for i in range(n):
            pointer = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack[-1]
                stack.pop()
                
                maxarea = max(height * (i - index), maxarea)
                pointer = index
            
            stack.append((pointer, heights[i]))

        while stack:
            index, height = stack[-1]
            stack.pop()
            maxarea = max(height * (n - index), maxarea)

        return maxarea
        

# Extends upon the solution of https://leetcode.com/problems/largest-rectangle-in-histogram/
# Perform this algorithm on each row, cumulating height as we're iterating rows, remembering
# to zero-out columns if the new row is 0 at these respective columns.