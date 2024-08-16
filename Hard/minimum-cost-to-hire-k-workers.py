# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Using greedy
        n = len(quality)

        # First order each worker based on their wage to quality ratio
        worker = sorted((w/q, q) for w, q in zip(wage, quality))

        # Pick the k-first workers based on ascending ratio
        quality, group = 0, []
        for i in range(k):
            quality += worker[i][1]

            # And store the group in a max-heap
            heappush(group, -worker[i][1])
        
        # Calculate initial minimum cost
        cost = worker[k-1][0] * quality

        # Then minimize cost by iteratively removing highest quality worker
        for i in range(k, n):
            # If the current worker has higher quality than anyone
            # in the group, skip it. It will be removed anyways
            if worker[i][1] > -group[0]:
                continue

            # Add current worker and remove highest quality worker
            quality += worker[i][1] + heappop(group)
            heappush(group, -worker[i][1])

            # Minimize cost
            cost = min(worker[i][0] * quality, cost)

        # Return the minimized cost for k workers
        return cost

# We can order the workers based on their wage to quality ratio. The higher
# the ratio, the more they want to get paid based on quality of work.
# Picking k workers, and paying them all by the same ratio as the worker
# with the highest wage to quality ratio will ensure they all get paid
# fairly following the rules given.

# We first calculate an initial pay, by greedily picking the k workers
# with the lowest wage to quality ratio.
# We can then compare this by other k-sized groups of workers by iteratively
# swapping out the current highest quality worker in the previous group.

# The result is the minimum pay out of all of these groups.