# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Using greedy
        happiness.sort(reverse=True)

        # Greedily pick the k-happiest children (with a current happiness > 0)
        result = sum(happiness[i] - i for i in range(k) if happiness[i] > i)
        return result