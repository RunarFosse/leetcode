# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)

        # Iterate every person's tickets
        time = 0
        for i in range(n):
            # If person i is before person k in line
            if i <= k:
                # Add either k's amount of tickets or i's amount
                time += min(tickets[i], tickets[k])
            
            # Else if person i is after person k
            else:
                # Add person k's up to last iteration, or all i's amount
                time += min(tickets[i], tickets[k]-1)
        
        # Return the accumulated time
        return time