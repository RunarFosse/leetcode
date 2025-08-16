# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Iterate the number
        n = floor(log(num))
        for i in reversed(range(n)):
            # And swap the first occuring 6 (from the left) to a 9
            digit = (num // pow(10, i)) % 10
            if digit == 6:
                return num + 3 * pow(10, i)
    
        # Otherwise, return the number as is
        return num