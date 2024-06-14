# Author: Runar Fosse
# Time complexity: O(m)
# Space complexity: O(m)

# where m is the maximum entry of nums

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # First count frequency of each number, remembering maximum entry
        frequencies, max_num = defaultdict(int), 0
        for num in nums:
            frequencies[num] += 1
            max_num = max(num, max_num)
        
        # Iterate from 0 to max_num, moving values following value increments
        increments = 0
        for i in range(max_num+1):
            if frequencies[i] <= 1:
                continue
                
            # If we are not at the end, keep "pushing" new entries forward
            if i < max_num:
                increments += frequencies[i]-1
                frequencies[i+1] += frequencies[i]-1

            # However if we are at the end, there will be no further 
            # "collisions" and we can greedily calculate increments
            else:
                increments += (frequencies[i]-1)*frequencies[i]//2
        
        # Return minimum number of increments
        return increments