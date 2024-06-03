# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Define a function for flipping a tuple
        flip = lambda e : tuple(reversed(e))
        
        # Then enumerate the scores, and sort in reversed order
        ranks = sorted(map(flip, enumerate(score)), reverse=True)

        # Then at last, assign ranks
        podium = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for i in range(len(score)):
            index = ranks[i][1]
            if i in podium:
                score[index] = podium[i]
            else:
                score[index] = str(i+1)
        
        # Return the final ranking
        return score