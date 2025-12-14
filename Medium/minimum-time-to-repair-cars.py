# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Using binary search

        # Count frequency of each mechanich's rank
        frequencies = defaultdict(int)
        for rank in ranks:
            frequencies[rank] += 1

        # Binary search minimal time to repair all cars
        left, right = 1, max(ranks) * cars * cars
        while left < right:
            pivot = (left + right) // 2

            # Check if mechanics can repair all cars within the allotted time
            current = 0
            for rank, frequency in frequencies.items():
                current += frequency * int(sqrt(pivot / rank))
            
            # And move bounds correspondingly
            if current < cars:
                left = pivot + 1
            else:
                right = pivot
            
        # Finally, return minimum time to repair cars
        return left

# Time to repair by cars mechanic: t = r * n ^ 2
# -> Repaired cars by mechanic: sqrt(t / r) = n