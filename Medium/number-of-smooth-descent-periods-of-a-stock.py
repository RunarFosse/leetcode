# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Using linear scan
        n = len(prices)

        # Iterate the array
        current, total = 0, 0
        for i in range(n):
            # Keep count of current smooth descending period
            if not i or prices[i] != prices[i - 1] - 1:
                current = 1
            else:
                current += 1
            
            # And add each to the total
            total += current

        # Finally, return the total number of smooth descent periods
        return total
