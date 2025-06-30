# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # First, count frequency of each number
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        # Then, for each entry in the frequencies dictionary
        longest = 0
        for num in frequencies.keys():
            # Check if the increment also exists
            if num + 1 in frequencies:
                # If it does, store longest subsequence
                longest = max(frequencies[num] + frequencies[num + 1], longest)
        
        # And return it
        return longest