# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mins = (100, 100)
        for price in prices:
            if price < mins[0]:
                mins = (price, mins[0])
            elif price < mins[1]:
                mins = (mins[0], price)
        
        total_cost = mins[0] + mins[1]
        if total_cost > money:
            return money
        
        return money - total_cost
        
# Simply find the 2 lowest numbers in the price array.