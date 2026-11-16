# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Turn the number string into a list
        number, digits = list(map(int, s)), len(s)

        # While we have more than k digits
        while digits > k:
            # Compute the current digit sum iteration
            current = 0
            for i in range(0, digits, k):
                group = sum(number[i:min(i + k, digits)])
                
                # Updating the number based on each group's digit sum
                divisor = pow(10, floor(log10(group))) if group > 0 else 1
                while divisor:
                    number[current] = group // divisor
                    group %= divisor
                    divisor //= 10
                    current += 1
            
            digits = current
        
        # Turn the resulting k digit number back into a string and return it
        result = "".join(map(str, number[:digits]))
        return result
