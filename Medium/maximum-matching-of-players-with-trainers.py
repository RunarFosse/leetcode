# Author: Runar Fosse
# Time complexity: O(mlog m + nlog n)
# Space complexity: O(m + n)

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Using greedy
        m, n = len(players), len(trainers)

        # Sort both players and trainers in ascending order
        players.sort()
        trainers.sort()

        # For each player
        matches, trainer = 0, 0
        for player in range(m):
            # If the current trainer is below their skill, find a new one
            while trainer < n and trainers[trainer] < players[player]:
                trainer += 1

            # And count a match
            if trainer < n:
                matches += 1
                trainer += 1
        
        # Finally, return the maximum number of matches
        return matches