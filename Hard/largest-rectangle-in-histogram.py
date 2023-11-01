# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
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

# Storing previous heights and their respective "smaller" indices in a stack
# Then when you reach a height smaller than the previous on the stack, calculate the
# maxareas of all numbers which satisfy the same condition in the front of the stack