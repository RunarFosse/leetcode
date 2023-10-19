# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        winners, rest = divmod(money - children, 7)
        if winners == children and not rest:
            return children
        if winners == children - 1 and rest == 3:
            return children - 2
        
        return min(winners, children - 1)