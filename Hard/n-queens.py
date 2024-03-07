# Author: Runar Fosse
# Time complexity: O(n!)
# Space complexity: O(n^2)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Using backtracking
        self.solutions = []
        self.solve([], 0, n)
        return self.solutions
    
    def solve(self, current: List[int], column: int, n: int) -> None:
        if column == n:
            # Solution is feasible! Add to solutions and backtrack 1 step
            self.solutions.append(self.create(current, n))
            return
        
        # Use current solution to identify infeasible positions
        infeasibles = set()
        for i, row in enumerate(current):
            infeasibles.add(row)
            infeasibles.add(row + (column - i))
            infeasibles.add(row - (column - i))

        # Then solve by placing a queen at every feasible position
        for row in range(n):
            if row in infeasibles:
                continue
            current.append(row)
            self.solve(current, column+1, n)
            current.pop()
    
    def create(self, current: List[int], n: int) -> List[List[str]]:
        # Use a given solution representation to construct a solution
        solution = []
        for column in range(n):
            spaces = []
            for row in range(n):
                spaces.append("Q" if current[column] == row else ".")
            solution.append("".join(spaces))
        
        return solution

# The solution representation of this problem can be represented using a single
# array. Every entry represents a queen, where the index is the current column,
# and the number stored in this position declares the row.

# A feasible solution looks like this (with details):
# 
#    A  B  C  D
#   [3, 1, 4, 2]

# As we can see, a solution will be feasible if and only if, for an entry q_i,
# the subsequent entry q_(i+1) is NOT equal to q_i, q_i + 1 or q_i - 1.

# These would be infeasible solutions:
# 
#    A  B  C  D         or          A  B  C  D
#   [3, 2, 4, 1]                   [3, 4, 2, 1]