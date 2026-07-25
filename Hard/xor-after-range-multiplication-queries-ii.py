# Author: Runar Fosse
# Time complexity: O(m + n sqrt(n))
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Using prefix sum
        n = len(nums)
        sqrt_n = isqrt(n)

        # Iterate the queries
        groups = [[] for _ in range(sqrt_n)]
        for left, right, k, value in queries:
            # For small k, group the queried range multiplications based on k
            if k < sqrt_n:
                groups[k].append((left, right, value))
                continue
            
            # Otherwise, k is large enough to efficiently apply directly
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * value) % self.mod
        
        # Then, iterate each of the groups
        for k in range(sqrt_n):
            if not groups[k]:
                continue

            # Creating a difference array holding range multiplications
            differences = [1] * (n + k)
            for left, right, value in groups[k]:
                # Multiply with the value to the left
                differences[left] = (differences[left] * value) % self.mod

                # Find the rightmost k-multiple after right
                end = ((right - left) // k + 1) * k + left

                # And multiply with the value's modular multiplicative inverse
                inverse = pow(value, self.mod - 2, self.mod)
                differences[end] = (differences[end] * inverse) % self.mod
            
            # Then, expand all multiplications at each k-step over array
            for i in range(k, n):
                differences[i] = (differences[i] * differences[i - k]) % self.mod
            
            # And apply multiplications to array
            for i in range(n):
                nums[i] = (nums[i] * differences[i]) % self.mod
        
        # Finally, compute and return the final XOR sum of the array
        return reduce(xor, nums)
