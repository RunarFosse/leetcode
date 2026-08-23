# Author: Runar Fosse
# Time complexity: O(m + log n)
# Space complexity: O(m + log n)

class Solution:
    mod = int(1e9 + 7)
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Using prefix sum

        # First, extract the powers of 2 from n
        powers = []
        for i in range(n.bit_length()):
            power = (1 << i)
            if n & power:
                powers.append(power)

        # Compute prefix product and multiplicative inverse
        products, inverses = [1], [1]
        for power in powers:
            products.append((power * products[-1]) % self.mod)

            # Computing modular multiplicative inverse using Fermat's little theorem
            inverses.append(pow(products[-1], self.mod - 2, self.mod))

        # Then, iterate the queries
        answers = []
        for left, right in queries:
            # Computing their subarray power product
            product = (products[right + 1] * inverses[left]) % self.mod
            answers.append(product)
        
        return answers
