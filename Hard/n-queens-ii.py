# Author: Runar Fosse
# Time complexity: O(n!)
# Space complexity: O(1)

class Solution:
    def totalNQueens(self, n: int) -> int:
        # Using backtracking
        self.solutions = 0
        self.solve([], 0, n)
        return self.solutions
    
    def solve(self, current: List[int], column: int, n: int) -> None:
        if column == n:
            # Solution is feasible! Add to solutions and backtrack 1 step
            self.solutions += 1
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

# This solution is heavily derived from n-queens (https://leetcode.com/problems/n-queens/)
# but without any actual solution creation.