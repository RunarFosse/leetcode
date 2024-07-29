# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        # For each of the soliders, count how many
        # teams they can be a part of
        teams = 0
        for i in range(1, n-1):
            # Count soldier strictly lower or higher rated
            # than current on the left in the array
            low_left, high_left = 0, 0
            for j in range(i):
                if rating[j] < rating[i]:
                    low_left += 1
                elif rating[j] > rating[i]:
                    high_left += 1
            
            # Count soldier strictly lower or higher rated
            # than current on the right in the array
            low_right, high_right = 0, 0
            for k in range(i+1, n):
                if rating[k] < rating[i]:
                    low_right += 1
                elif rating[k] > rating[i]:
                    high_right += 1
            
            # Add possible teams current soldier can be a part of
            teams += low_left * high_right
            teams += high_left * low_right

        # Return total number of possible teams
        return teams