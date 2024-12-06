# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Using greedy

        # Store banned words in a set
        banned = set(banned)

        # Iterate n from 0
        count = 0
        for i in range(1, n+1):
            # If we cannot add more to sum, break
            if maxSum < i:
                break
            
            # If i is banned, skip
            if i in banned:
                continue
            
            # If not, add to sum
            maxSum -= i
            count += 1
        
        # Return final count
        return count