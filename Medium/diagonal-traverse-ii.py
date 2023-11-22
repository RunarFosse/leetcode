# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = []
        queue = deque([(0,0)])
        while queue:
            row, column = queue.popleft()
            diagonals.append(nums[row][column])

            # If at beginning of a row, add next row
            if column == 0 and row + 1 < len(nums):
                queue.append((row + 1, column))
            
            # If there are more numbers in this current row, and them in end of queue
            if column + 1 < len(nums[row]):
                queue.append((row, column + 1))

        return diagonals