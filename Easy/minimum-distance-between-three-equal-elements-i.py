# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # Iterate the array
        minimum, indices = 1e9, defaultdict(deque)
        for i in range(n):
            # Add the current index to element indices dictionary 
            num = nums[i]
            indices[num].append(i)
            
            # If we have three indices stored, then we have a good tuple
            if len(indices[num]) < 3:
                continue
            
            # Compute the distance of this good tuple
            j, k, _ = indices[num]
            distance = abs(i - j) + abs(j - k) + abs(k - i)

            # Store the minimum distance
            minimum = min(distance, minimum)

            # And remove the first index of this element from dictionary
            indices[num].popleft()

        # Finally, return the minimum possible distance of a good tuple, if it exists
        return minimum if minimum < 1e9 else -1