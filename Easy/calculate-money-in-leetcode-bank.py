# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def totalMoney(self, n: int) -> int:
        # Using analytical deduction
        weeks, days = divmod(n, 7)
        return 21 * weeks + (7 * weeks * (weeks + 1) + days * (2*weeks + days + 1)) // 2
        

# He starts by putting in $1 on monday. That means his first week looks like this:
# $1 - $2 - $3 - $4 - $5 - $6 - $7  = 28
# Then the next week he starts by putting in $1 more than last monday, making it:
# $2 - $3 - $4 - $5 - $6 - $7 - $8  = 35
# Next again:
# $3 - $4 - $5 - $6 - $7 - $8 - $9  = 42
#
# Following this pattern, and that we have:
#
# n mod 7 == What day in the week he stops on
# n div 7 == How many weeks he puts in money for

# We can conclude that the answer will be:
# amount = 21 * weeks + 7 * sum(1..weeks) + days*weeks + sum(1..days)
# which can be compressed down to:
# amount = 21 * weeks + 7 * (weeks^2 - weeks) / 2 + days * (2*weeks + days - 1) / 2
# (for less divisions and no exponentiation, we have:)
# amount = 21 * weeks + (7 * weeks * (weeks + 1) + days * (2*weeks + days + 1)) // 2