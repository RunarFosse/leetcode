# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Using BFS
        n = len(status)

        # Add all initial boxes to the queue, and start BFS
        candy, queue = 0, deque(initialBoxes)
        while queue:
            # Pick the next box
            box = queue.popleft()

            # If we cannot open the box, set its status to -1 and continue
            if status[box] == 0:
                status[box] = -1
                continue

            # Retrieve the candy from it
            candy += candies[box]

            # Open every box with their keys
            for key in keys[box]:
                # If we've seen the box, but couldn't open, add it to the queue
                if status[key] == -1:
                    queue.append(key)
                status[key] = 1

            # And add all contained boxes
            for contained in containedBoxes[box]:
                queue.append(contained)
        
        # Finally, return all the gathered candy
        return candy