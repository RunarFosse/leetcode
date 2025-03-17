# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Iterate the array, counting element frequencies
        frequencies = [0] * 501
        for num in nums:
            frequencies[num - 1] += 1
        
        # Return True if all elements occur an even amount of times
        return all(map(lambda freq: freq % 2 == 0, frequencies))