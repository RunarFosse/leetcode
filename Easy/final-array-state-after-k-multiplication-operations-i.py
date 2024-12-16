# Author: Runar Fosse
# Time complexity: O(n + klog n)
# Space complexity: O(n)

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Using heap
        n = len(nums)

        # First create a min-heap
        queue = [(nums[i], i) for i in range(n)]
        heapify(queue)

        # Then perform k operations
        for _ in range(k):
            _, i = heappop(queue)
            nums[i] *= multiplier
            heappush(queue, (nums[i], i))
        
        # And return the new array
        return nums
