# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Using greedy
        max_sum = 0

        # For each node in the tree
        positive_differences, min_distance = 0, 1e9
        for num in nums:
            # Add value of node to maximum sum
            max_sum += num

            # Then calculate the difference from performing XOR with k
            difference = (num ^ k) - num

            # If this difference is positive, add to sum
            if difference > 0:
                max_sum += difference
                positive_differences += 1

            # And store minimum distance from node value for all differences
            min_distance = min(abs(difference), min_distance)

        # If the number of positive differences is odd after termination,
        # subtract the smallest distance value of a node from sum
        if positive_differences % 2:
            max_sum -= min_distance
        
        # Return maximum possible value sum
        return max_sum