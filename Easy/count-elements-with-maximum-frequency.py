# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count frequencies of each element
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        # Then iterate, storing current maximum frequency
        max_frequency, elements = 0, 0
        for frequency in frequencies.values():
            if frequency > max_frequency:
                max_frequency = frequency
                elements = frequency
            elif frequency == max_frequency:
                elements += frequency
        
        # Return elements with said frequency
        return elements