# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using prefix/suffix product
        n = len(nums)
        products = [1] * n

        # Calculate running prefix and initialize products
        prefix = 1
        for i in range(n):
            products[i] *= prefix
            prefix *= nums[i]
        
        # Then calculate running suffix and multiply with products
        suffix = 1
        for i in reversed(range(n)):
            products[i] *= suffix
            suffix *= nums[i]

        # This gives us our product of array except self for every element
        return products