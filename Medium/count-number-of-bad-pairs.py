# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0

        # Iterate the numbers
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            # Compute how many good pairs we can make
            difference = i - num
            good_pairs = seen[difference]

            # Turn into bad_pairs
            bad_pairs += i - good_pairs

            # Add current difference to seen
            seen[difference] += 1
    
        # Finally, return the number of bad pairs
        return bad_pairs



# Instead of counting bad pairs, it would be more efficient to count good
# pairs, and then compute (bad pairs) = (all pairs) - (good pairs).

# We have a pair is good if: j - i == nums[j] - nums[i].
# This can be rewritten as: i - nums[i] == j - nums[j].