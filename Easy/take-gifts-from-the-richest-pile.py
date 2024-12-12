# Author: Runar Fosse
# Time complexity: O(n + klog n)
# Space complexity: O(1)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)

        # Turn gifts into a maxheap
        for i in range(n):
            gifts[i] *= -1
        heapify(gifts)

        # Then simulate picking of gifts
        for _ in range(k):
            # Pick the most gifts
            current = -heappop(gifts)

            # Replace with the floor of the square root
            heappush(gifts, -floor(sqrt(current)))
        
        # Finally, return the remaining gifts
        return -sum(gifts)