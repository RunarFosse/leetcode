# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Count occurence of each number
        occurences = {i+1: 0 for i in range(n)}
        for num in nums:
            occurences[num] += 1
        
        # Then it is trivial to extract repeated/missing numbers
        repeated, missing = 0, 0
        for num, occurence in occurences.items():
            if occurence == 0:
                missing = num
            if occurence == 2:
                repeated = num
        
        return [repeated, missing]