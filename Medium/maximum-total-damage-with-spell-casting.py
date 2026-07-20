# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Using dynamic programming
        n = len(power)

        # First, sort the spells in ascending order of damage
        power.sort()

        # Then, iterate the spells, keeping rolling spell damage candidates
        damage1, damage2, damage3, total = power[0], 0, 0, 0
        for i in range(1, n):
            # Every spell of the same damage can be cast together
            if power[i] == power[i - 1]:
                damage1 += power[i]
            
            # If the current spell deals 1 more damage than the previous
            elif power[i] == power[i - 1] + 1:
                # Only spells that do sufficiently less damage can be combined with this
                total = max(damage3, total)

                # Shift the other rolling candidates 1 damage forward
                damage3, damage2 = damage2, damage1

                # And start counting current damage candidate anew
                damage1 = total + power[i]
            
            # If the current spell deals 2 more damage
            elif power[i] == power[i - 1] + 2:
                # We can combine with even more spells
                total = max(damage2, damage3, total)

                # Updating candidates with this higher gap
                damage3, damage2 = damage1, max(damage1, total)
                damage1 = total + power[i]

            # If it deals even more damage
            else:
                # Then any previous damage spells can be combined with this
                total = max(damage1, damage2, damage3, total)

                # Resetting candidate values to account for this
                damage3, damage2 = total, total
                damage1 = total + power[i]
        
        # Finally, recompute our final maximum total damage value
        total = max(damage1, damage2, damage3, total)
        
        # And return the maximum total damage we can do with spells
        return total


# opt(i) - The maximum damage that can be dealt using spells
#          at or after index i, in the sorted power array.

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = max(spells * damage + opt(next_j), opt(next_i))
#          where damage = power[i]
#                next_i = bisect_left(power, damage + 1)
#                next_j = bisect_left(power, damage + 3)
#                spells = next_i - i

# No. states = n
# Time complexity per state -> O(log n)
# Total time complexity => O(nlog n)

# The recurrence can be implemented with four rolling candidates, allowing us to 
# eliminate any binary search. After sorting the spells, the dynamic programming scan
# takes O(n) time, while sorting still makes the total complexity O(nlog n).