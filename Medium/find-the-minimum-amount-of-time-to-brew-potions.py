# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # Using prefix sum
        n = len(skill)
        
        # Iterate every potion
        times = [0] * n
        for potion in mana:
            # Brew the potion and compute finish time
            time = times[0]
            for i in range(n):
                time = max(time, times[i]) + skill[i] * potion
            
            # Use this time and compute every wizard's new free time
            times[n - 1] = time
            for i in reversed(range(n - 1)):
                # Knowing the wizard after needs to be free whenever we finish our part
                times[i] = times[i + 1] - skill[i + 1] * potion
        
        # Finally, return the moment the last wizard is finished with the last potion
        return times[n - 1]
