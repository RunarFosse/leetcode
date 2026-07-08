# Author: Runar Fosse
# Time complexity: O(mlog n + n)
# Space complexity: O(m + n)

class Solution:
    mod = int(1e9 + 7)
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # Using prefix sum

        # First, compute prefix sum and x, as well as number of zeros
        prefixes = [(0, 0, 0)]
        x, sum, zeros = 0, 0, 0
        for c in s:
            digit = int(c)
            if digit:
                x = (x * 10 + digit) % self.mod
                sum = (sum + digit) % self.mod
            else:
                zeros += 1
            prefixes.append((x, sum, zeros))
        
        # Then, iterate each of the queries
        answer = []
        for left, right in queries:
            # Extract the information from prefix sums
            exponent = (right + 1 - left) - (prefixes[right + 1][2] - prefixes[left][2])
            multiplier = self.modexp(10, exponent)
            x = (prefixes[right + 1][0] - prefixes[left][0] * multiplier) % self.mod
            sum = prefixes[right + 1][1] - prefixes[left][1]

            # And compute the result
            answer.append(x * sum % self.mod)
        
        # Finally, return the answer to each of the queries
        return answer

    def modexp(self, base: int, exponent: int) -> int:
        # Fast modular exponentiation algorithm
        result = 1
        while exponent:
            if exponent & 1:
                result = result * base % self.mod
            base = base * base % self.mod
            exponent >>= 1
        return result
