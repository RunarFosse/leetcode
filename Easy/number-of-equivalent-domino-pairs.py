# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Iterate the dominoes
        frequencies = defaultdict(int)
        for top, bottom in dominoes:
            # Swap them if top is larger than bottom
            if top > bottom:
                top, bottom = bottom, top
            
            # Increment domino frequency
            frequencies[(top, bottom)] += 1
        
        # Finally, count and return the number of pairs
        return sum(freq*(freq-1)//2 for freq in frequencies.values())


# Given x equal dominoes, the number of pairs we can create is equal
# to the sum of all number in [1, .., x - 1]. 