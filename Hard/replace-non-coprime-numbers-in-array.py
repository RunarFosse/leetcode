# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

# where m is the maximum value in the array

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # Using stack

        # Iterate the array
        stack = []
        for num in nums:
            # While there are numbers on the stack
            while stack:
                # If the current pair are coprime
                divisor = gcd(num, stack[-1])

                # Break the loop
                if divisor == 1:
                    break
                
                # Otherwise, replace the current with their least common multiple
                num = (num * stack.pop()) // divisor
            
            # Then, place the resulting number onto the stack
            stack.append(num)
        
        # Return the final resulting array
        return stack


# We only apply operations to pairs of numbers which are non-coprime.
# This means they have a gcd > 1.

# The least common multiple of any two numbers can easily be computed as,
# for the pair (a, b):
# lcm(a, b) = (a * b) / gcd(a, b)

# As we've already computed the gcd, this makes the process incredibly simple.