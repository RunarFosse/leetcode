# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Using dynamic programming
        return self.waviness(num2) - self.waviness(num1 - 1)
    
    def waviness(self, num: int) -> int:
        # If the given number is less than or equal to zero, default it to zero
        if num <= 0:
            return 0
        
        # First, extract all the digits in the given bound num
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.reverse()
        n = len(digits)

        # Then, declare the opt function
        @functools.cache
        def opt(i: int, previous: Tuple[Optional[int], Optional[int]], tight: bool) -> Tuple[int, int]:
            # If we are at the end
            if i == n:
                # We have a valid number with zero waviness
                return (0, 1)
            
            # Declare the current digit limit based on tightness
            limit = digits[i] if tight else 9

            # As well as if we've started generating a number
            started = previous[0] is not None

            # Iterate all the valid digits below or at the limit
            waviness, count = 0, 0
            for digit in range(limit + 1):
                # If we have not started, and digit is a zero
                if not started and digit == 0:
                    # Continue with leading zeros
                    child_waviness, child_count = opt(i + 1, previous, False)
                    waviness += child_waviness
                    count += child_count
                    continue
                
                # If we have only not started, start
                if not started:
                    child_waviness, child_count = opt(i + 1, (digit, None), tight and digit == limit)
                    waviness += child_waviness
                    count += child_count
                    continue
                
                # Otherwise, continue recursing and computing waviness of rest of number
                child_waviness, child_count = opt(i + 1, (digit, previous[0]), tight and digit == limit)
                waviness += child_waviness
                count += child_count

                # If both two digits are set, we can compute waviness
                if previous[1] is not None:
                    isPeak = previous[1] < previous[0] > digit
                    isValley = previous[1] > previous[0] < digit
                    if isPeak or isValley:
                        # If either a peak or valley, we have a waviness per valid child
                        waviness += child_count
                
            # Return waviness and count
            return waviness, count

        # Finally, return the total waviness below and including the bound num
        waviness, _ = opt(0, (None, None), True)
        return waviness


# opt(i, previous, tight) - Total amount of numbers with their waviness under
#                                    a given number num, modifying digit at index i
#                                    with the previous last two digits. Tight denotes
#                                    whether previous digits equal the bound num.

# N.o. states = log n * 11 * 11 * 2
# Runtime per state -> O(1)
# Total time complexity => O(log n)