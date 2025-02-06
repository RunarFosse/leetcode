# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # Compute all product pairs
        products = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                products[nums[i] * nums[j]] += 1
        
        # Then for each of the products
        count = 0
        for product, frequency in products.items():
            # Count possible combinations of products
            combinations = (frequency - 1) * frequency // 2

            # And add combination of elements (a, b, c, d) per combination
            count += combinations * 8
        
        # Return this total count
        return count


# Finding tuples a * b = c * d would be equivalent to finding the pairs
# e = f where e and f are products of numbers in the original array.
# From this we can easily count combinations without overlap.