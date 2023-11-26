# Author: Runar Fosse
# Time complexity: O(mnlog n)
# Space complexity: O(n)

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Using stack
        m, n = len(matrix), len(matrix[0])

        max_rectangle = 0
        cumulative_row = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                # Cumulate new row
                if not matrix[i][j]:
                    cumulative_row[j] = 0
                else:
                    cumulative_row[j] += 1
            
            # Perform Largest Rectangle algorithm
            sorted_row = sorted(cumulative_row)
            max_rectangle = max(self.largestRectangleArea(sorted_row), max_rectangle)

        return max_rectangle

    # Directly copied from "https://leetcode.com/problems/maximal-rectangle/"
    # (and consequently "https://leetcode.com/problems/largest-rectangle-in-histogram/")
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

# This question again builts upon https://leetcode.com/problems/maximal-rectangle/
# Use the same algorithm we did in that problem, but sort every row before calculating.
# If we sort using python's sorted() function we will not override the ordering of
# the columns, allowing us to continue the algorithm on the next row without modification.