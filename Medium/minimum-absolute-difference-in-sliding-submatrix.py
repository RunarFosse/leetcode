# Author: Runar Fosse
# Time complexity: O(kmnlog k)
# Space complexity: O(mn)

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Using sliding window
        m, n = len(grid), len(grid[0])

        # Store the current sliding window values and differences
        self.values, self.differences = SortedSet(), SortedList()
        self.frequencies = defaultdict(int)

        # Populate the window with the first k x k submatrix
        for i in range(k):
            for j in range(k):
                self.expandWindow(grid[i][j])

        # Then, iterate every such submatrix
        rows, columns = m - k + 1, n - k + 1
        submatrices = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            # Slither down the matrix, back and forth
            order, leftwards = range(columns), (i % 2 == 1)
            if leftwards:
                order = reversed(range(k - 1, n))
            
            # Then, iterate and expand the window columnwise
            for j in order:
                # If we have a difference in the submatrix, get the minimum
                if self.differences:
                    submatrices[i][j - k + 1 if leftwards else j] = self.differences[0]

                # If we've reached the final column, break early
                if (leftwards and j == k - 1) or (not leftwards and j == columns - 1):
                    break
                
                # Then, compute the column entering and leaving the sliding window
                leaving, entering = j, j + k
                if leftwards:
                    leaving, entering = j, j - k
                
                # And shrink + expand the window accordingly
                for row in range(i, i + k):
                    self.shrinkWindow(grid[row][leaving])
                    self.expandWindow(grid[row][entering])
            
            # If we are at the end, break early
            if i == rows - 1:
                break
            
            # Then, compute the range of columns to add and remove from old and new row
            order = range(n - k, n)
            if leftwards:
                order = range(k)

            # And at last, shrink + expand the window according to this row change
            for column in order:
                self.shrinkWindow(grid[i][column])
                self.expandWindow(grid[i + k][column])

        # Finally, return the minimum absolute difference of each k x k submatrix
        return submatrices
    
    def expandWindow(self, value: int):
        # Expand the sliding window with a new value
        self.frequencies[value] += 1
        
        # If the value already is in the window, there is nothing to add
        if value in self.values:
            return
        
        # Otherwise, get the index of where it will be inserted
        index = self.values.bisect_left(value)

        # If there is one, remove the previous (now larger) difference
        if 0 < index < len(self.values):
            previous = self.values[index] - self.values[index - 1]
            self.differences.remove(previous)

        # And add the new existing differences
        if index > 0:
            difference = value - self.values[index - 1]
            self.differences.add(difference)
        if index < len(self.values):
            difference = self.values[index] - value
            self.differences.add(difference)
        
        # Also, add the value to the set
        self.values.add(value)
    
    def shrinkWindow(self, value: int):
        # Shrink the sliding window, removing a value
        self.frequencies[value] -= 1

        # If there are more of the same value, do nothing
        if self.frequencies[value] > 0:
            return
        
        # Otherwise, get the value's index
        index = self.values.bisect_left(value)

        # Remove its existing differences
        if index > 0:
            difference = value - self.values[index - 1]
            self.differences.remove(difference)
        if index < len(self.values) - 1:
            difference = self.values[index + 1] - value
            self.differences.remove(difference)
        
        # And replace it with a possible new existing difference
        if 0 < index < len(self.values) - 1:
            new = self.values[index + 1] - self.values[index - 1]
            self.differences.add(new)
        
        # Also, remove the value from the set
        self.values.remove(value)
