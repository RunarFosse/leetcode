# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # Iterate the array
        binary, answer = 0, []
        for bit in nums:
            # Keeping track of the current prefix binary number, modulo five
            binary = ((binary << 1) | bit) % 5

            # If it now is divisible by five, it will be equal to zero
            answer.append(binary == 0)
        
        # Finally, return all the answers
        return answer