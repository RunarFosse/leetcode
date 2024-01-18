# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        triplets = set()
        for i in range(n):
            current_pairs = set()
            for j in range(i+1, n):
                # If the negative version of the current number exists, we
                # have found a triplet
                if -nums[j] in current_pairs:
                    # Sort the triplet to prevent duplicate triplets
                    triplet = sorted([nums[i], -nums[j] - nums[i], nums[j]])
                    triplets.add(tuple(triplet))

                current_pairs.add(nums[i] + nums[j])
        
        return list(triplets)
    
# This can be solved by solving two sum for each number in the suffix array of nums

# Not, we are sorting each triplet, but as they only contain three values, this
# is equivalent to constant time. (O(3log 3) == O(1))