# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Using sliding window

        # Iterate every number in the given range
        waviness = 0
        for num in range(num1, num2 + 1):
            # Iterate all the digits in the current number
            digits = deque([])
            while num:
                digits.append(num % 10)
                num //= 10

                # If we have three digits inside the window
                if len(digits) == 3:
                    # Check if peak or valley, and if so,increment waviness
                    isPeak = digits[0] < digits[1] > digits[2]
                    isValley = digits[0] > digits[1] < digits[2]
                    if isPeak or isValley:
                        waviness += 1

                    # And pop the last off the window
                    digits.popleft()
        
        # Finally, return the total waviness in the range
        return waviness
