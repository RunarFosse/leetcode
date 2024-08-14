# Author: Runar Fosse
# Time complexity: O(nlog n + nlog m)
# Space complexity: O(n)

# where m is the maximum distance between any two elements

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Using binary search
        self.n = len(nums)

        # Sort the input array
        nums.sort()

        # Binary search over the maximum distance among all pairs
        left, right = 0, (nums[-1] - nums[0])
        while left < right:
            distance = (left + right) // 2

            # Count how many pairs exist with a distance smaller or equal
            pairs = self.countPairsWithMaxDistance(distance, nums)
            
            # Move the pointers accordingly
            if pairs < k:
                left = distance+1
            else:
                right = distance

        return left
        
    def countPairsWithMaxDistance(self, distance: int, nums: List[int]) -> int:
        # Using sliding window
        pairs = 0
        p1, p2 = 0, 0
        while p2 < self.n:
            # While the maximum distance within the window is greater,
            # shrink it
            while nums[p2] - nums[p1] > distance:
                p1 += 1
            
            # Then count pairs, and extend the window
            pairs += p2 - p1
            p2 += 1

        return pairs