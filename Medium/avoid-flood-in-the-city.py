# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Using greedy
        n = len(rains)

        # Keep track of what day each lake got flooded at
        flooded = {}

        # Then iterate all the rains
        answer, drys = [-1] * n, SortedList()
        for i in range(n):
            # If we have a dry day
            if rains[i] == 0:
                # Store dry as a wildcard, that can be used in the future
                drys.add(i)
                answer[i] = 1
                continue
            
            # Otherwise, if the current lake already is flooded
            if rains[i] in flooded:
                # Check if we can dry it before
                index = drys.bisect_right(flooded[rains[i]])
                if index >= len(drys):
                    # If we can't, flooding is inevitable
                    return []
                
                # If not, retroactively dry this lake
                answer[drys.pop(index)] = rains[i]
            
            # Lastly, flood the lake (again)
            flooded[rains[i]] = i
        
        # Finally, return the answer ensuring no lake floods
        return answer
