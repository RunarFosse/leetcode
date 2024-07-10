# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Count depth away from main directory
        depth = 0
        for operation in logs:
            # Don't move if operation says to stay
            if operation == "./" or (operation == "../" and not depth):
                continue
            
            # If not, change depth based on operation
            depth += -1 if operation == "../" else 1
        
        # Return current depth
        return depth