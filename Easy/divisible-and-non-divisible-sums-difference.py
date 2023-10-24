# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ndivm = n // m
        num2 = (m)*(ndivm)*(ndivm+1)/2
        num1 = (n)*(n+1)/2 - num2
        return int(num1 - num2)
    
# Numbers divisible by m in [1,n] is equal to ndivm := n // m.
# Sum of all numbers divisible by m is then m + 2*m + 3*m + ... + ndivm*m 
# which is equal to m * sum([1,ndivm]).
# Sum can be calculated in O(1) time through sum([1,x]) = (x)*(x+1)/2
# Thus, num2 = (m)*(ndivm)*(ndivm+1)/2
# Then we know that the rest cant be divisible by m, thus sum([1,n]) - num2 = num1
# or num1 = (n)*(n+1)/2 - num2