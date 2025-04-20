# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Store frequency of each answer
        frequencies = defaultdict(int)
        for answer in answers:
            frequencies[answer] += 1
        
        # Then count how many rabbits for each entry to add up
        rabbits = 0
        for number, frequency in frequencies.items():
            rabbits += ceil(frequency / (number + 1)) * (number + 1)
        
        # Finally, return the minimum number of rabbits
        return rabbits