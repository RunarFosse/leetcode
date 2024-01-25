# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # If a number is less than the other, padd the smaller with leading 0s
        n, m = len(num1), len(num2)
        if n < m:
            num1 = "0" * (m - n) + num1
        if m < n:
            num2 = "0" * (n - m) + num2

        result, carry = "", 0
        # For each digit in the numbers
        for i in range(1, max(n, m) + 1):
            # Add both digits + carry
            sum = int(num1[-i]) + int(num2[-i]) + carry
            carry = 0

            # If sum is >= 10, set carry to 1 and sum to remainder
            if sum >= 10:
                carry = 1
                sum -= 10

            # Concatenate current digit sum infront of number
            result = str(sum) + result

        # If carry is 1 at the end, add leading 1
        if carry:
            result = "1" + result

        return result

        
# This can easily be solved using the addition algorithm from second grade.

# This problem however requires us to convert each digit into integers. 
# This is different from converting the inputs to integers directly, thus it
# does not break the solution requirements.