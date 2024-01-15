# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)

        # Guarantee all players (even with 0 losses) are in the dictionary
        for winner, _ in matches:
            loss[winner] = 0
        
        # Count losses per player
        for _, loser in matches:
            loss[loser] += 1
        
        # Compute and sort the solution
        result = ([], [])
        for player, losses in loss.items():
            if losses <= 1:
                result[losses].append(player)
        return (sorted(result[0]), sorted(result[1]))