# Author: Runar Fosse
# Time complexity: O(nlog t)
# Space complexity: O(n)

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Using greedy
        n = len(num)

        # First, compute the residue from prime factorizing t into factors less than 10
        residue = t
        for prime in [2, 3, 5, 7]:
            while residue % prime == 0:
                residue //= prime

        # If t is not yet factorized, we can not represent multiples using digit products
        if residue != 1:
            return "-1"
        
        # Otherwise, iterate the number
        digits, residues, end = list(num), [t] + [0] * n, n
        for i in range(n):
            # If we ever encounter a zero, break out early
            if digits[i] == "0":
                end = i + 1
                break

            # Computing remaining residue of t after each digit
            residues[i + 1] = residues[i] // gcd(int(digits[i]), residues[i])
        
        # If the last residue remaning is the identity
        if residues[-1] == 1:
            # Then the digit product of num is already a multiple of t
            return num
        
        # Otherwise, iterate the previous digit substring again from behind
        for i in reversed(range(end)):
            # And, through backtracking, minimize num whilst making it t-divisible
            for digit in range(int(digits[i]) + 1, 10):
                digits[i] = str(digit)

                # Compute the new residue with this new digit
                residue = residues[i] // gcd(digit, residues[i])

                # And try backfilling the remainder of the string, fully dividing t
                current = 9
                for j in reversed(range(i + 1, n)):
                    while residue % current != 0:
                        current -= 1
                    digits[j] = str(current)
                    residue //= current
                
                # If we've found a backtrack solution fully dividing t
                if residue == 1:
                    # Then we've found the minimum number with digit product t-divisible
                    return "".join(digits)

        # Otherwise, there is no solution with the same number of digits as num, and we
        # must greedily construct the smallest number dividing t with more digits
        digits, residue = [], t
        for digit in reversed(range(2, 10)):
            while residue % digit == 0:
                digits.append(str(digit))
                residue //= digit
        
        # If the resulting number ends in fewer digits than num, backfill the remaining
        padding = max(n + 1 - len(digits), 0)
        digits.extend(["1"] * padding)
        digits.reverse()
        
        # Finally, return this resulting number equal or bigger than num, and dividing t
        return "".join(digits)
