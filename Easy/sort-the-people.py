# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        # Sort indices based on heights in descending order
        indices = sorted(range(n), key=lambda i: -heights[i])

        # Return the names, in the above order
        return [names[i] for i in indices]