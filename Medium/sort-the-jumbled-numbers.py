# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # First define a function to map a given number to its other version
        def mapNumber(num: int) -> int:
            mapped, multiplier = mapping[num % 10], 10
            while num // multiplier:
                # Get the current last digit 
                digit = (num // multiplier) % 10

                # Add its mapping
                mapped += mapping[digit] * multiplier

                # And exponentiate multiplier
                multiplier *= 10
            return mapped
        
        # Then sort the numbers, using this mapping as its key
        nums.sort(key=mapNumber)

        # And return it
        return nums