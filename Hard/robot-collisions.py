# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # First sort robots based on position in ascending order
        indices = sorted(range(len(positions)), key=lambda i: positions[i])
        original = [0] * len(positions)

        # Iterate robots from the left, keeping track of current
        # "alive" robots going right. Also store known survivors.
        rights, survivors = [], []
        for i in indices:
            health = healths[i]
            # If the robot is going right, store it for later
            if directions[i] == "R":
                rights.append([i, health])
            
            # If it is going left, check if it survives against right robots
            else:
                while rights and health:
                    # If it has more health, it survives, but loses 1 point
                    if health > rights[-1][1]:
                        rights[-1][1] = 0
                        health -= 1
                    # If less, make right robot lose 1 health and break
                    elif health < rights[-1][1]:
                        rights[-1][1] -= 1
                        health = 0
                    # If equal, give both 0 health
                    else:
                        rights[-1][1] = 0
                        health = 0
                    
                    # If right robot has 0 health, destroy it
                    if not rights[-1][1]:
                        rights.pop()
                
                # Then if health is greater than 0, store as survivor
                if health:
                    survivors.append([i, health])

        # Combine with the surviving right-moving robots
        rights.reverse()
        survivors += rights

        # And return the robots in the same order as given
        result = [None] * len(positions)
        for index, health in survivors:
            result[index] = health
        return [health for health in result if health]
