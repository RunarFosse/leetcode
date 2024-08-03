# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Count element frequency of target
        frequencies = [0] * 1000
        for num in target:
            frequencies[num-1] += 1
        
        # Then decrement frequencies of arr
        for num in arr:
            frequencies[num-1] -= 1
        
        # If all remaining frequencies are 0, arrays can be equal
        return not any(frequencies)
        
# If two arrays are permutations of eachother, they can be made equal
# through such "reversing of subarrays". Therefore this question
# asks us to check if two arrays are permutations of eachother.
# This is easily verified by checking they contain equal element occurences.