# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Iterate the operations, computing the resulting value of X
        return sum(1 if operation[1] == "+" else -1 for operation in operations)