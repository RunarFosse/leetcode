# Author: Runar Fosse
# Time complexity: O((m + n)log m)
# Space complexity: O(m + n)

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Using greedy
        m = len(potions)

        # Sort the potions in ascending order
        potions.sort()

        # Then, iterate the spells
        pairs = []
        for spell in spells:
            # Compute the lowest potion strength to be successful
            potion = success / spell

            # And count the number of potions with a higher strength
            count = m - bisect_left(potions, potion)
            pairs.append(count)
        
        # Finally, return the number of valid pairs for each spell
        return pairs
