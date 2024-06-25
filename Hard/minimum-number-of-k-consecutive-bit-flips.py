# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Using greedy
        n = len(nums)

        # Iterate the bitstring
        flips = 0
        history = deque([])
        for i in range(n):
            # First, remove "out of range" flips from history
            if history and history[0] <= i-k:
                history.popleft()

            # If the current element "should be" 0
            should_flip = len(history) % 2
            if not (nums[i] + should_flip) % 2:
                # Flip it and the k-1 next elements
                history.append(i)

                # If there are less than k elements remaining, return -1
                if i+k > n:
                    return -1

                # Finally increment flips
                flips += 1
        
        # Return the number of flips
        return flips


# Greedily flip the first bit if it is equal to 0 and iterate. We then do this
# until we reach the end of the array. If the result is that all elements are
# equal to 1, return the number of flips. If not, return -1.

# For an easy optimization we iterate the elements one by one, keeping
# a track of current flips and decrementing it based on a sliding window
# of flip histories.