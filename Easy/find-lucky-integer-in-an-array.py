# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Compute frequency of each number
        frequencies = defaultdict(int)
        for num in arr:
            frequencies[num] += 1
        
        # Then iterate the numbers, storing largest lucky integer
        lucky = -1
        for num, frequency in frequencies.items():
            if num == frequency:
                lucky = max(num, lucky)
        return lucky