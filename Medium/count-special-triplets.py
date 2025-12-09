# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def specialTriplets(self, nums: List[int]) -> int:
        # Using prefix sum
        n = len(nums)

        # Keep a prefix/suffix frequency count of elements in the array
        prefix, suffix = defaultdict(int), defaultdict(int)
        for num in nums:
            suffix[num] += 1

        # Then iterate the array at j
        triplets = 0
        for j in range(n):
            num = nums[j]
            suffix[num] -= 1

            # Count how many (num * 2) that exist before and after
            lefts = prefix[num * 2]
            rights = suffix[num * 2]

            # And count number of special triplets exist at this j
            triplets = (triplets + lefts * rights) % self.mod

            prefix[num] += 1

        # Finally, return the number of special triplets in the array
        return triplets
        