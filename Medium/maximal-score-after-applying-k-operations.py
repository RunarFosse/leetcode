# Author: Runar Fosse
# Time complexity: O(n + klog n)
# Space complexity: O(1)

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Using max heap
        score = 0

        # Turn the nums array into a max heap
        nums = list(map(lambda n: -n, nums))
        heapify(nums)
        
        # Perform k operations
        for _ in range(k):
            # Pick the maximum element from heap
            number = -heappop(nums)

            # Increment score
            score += number

            # And place element back into heap
            heappush(nums, -ceil(number / 3))
        
        # Finally return score
        return score