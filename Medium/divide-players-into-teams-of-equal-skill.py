# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Using two pointers
        frequencies = [0] * 1000

        # First compute the frequency of every skill
        # keeping track of minimum and maximum skill
        max_skill, min_skill = 0, 1e9
        for player in skill:
            frequencies[player - 1] += 1
            min_skill = min(player, min_skill)
            max_skill = max(player, max_skill)

        # Then team up the worst and best players, to make it most balanced
        equal_skill = min_skill + max_skill
        total_chemistry = 0
        for i in range(1000):
            if not frequencies[i]:
                continue
            
            # If we cannot team up such that every team is equal, return -1
            other_skill = equal_skill - i - 1
            if frequencies[other_skill - 1] != frequencies[i]:
                return -1

            # Compute chemistry and decrement frequencies
            if i == other_skill - 1:
                total_chemistry += (i + 1) ** 2 * frequencies[i] // 2
            else:
                total_chemistry += (i + 1) * other_skill * frequencies[i]
            frequencies[i] = 0
            frequencies[other_skill - 1] = 0
        
        # If every team is equal, return the total chemistry
        return total_chemistry