# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Store each balls current colour
        balls = {}

        # Store the number of balls per colour, and total distinct colours
        colours = defaultdict(int)
        distincts = 0

        # For each query
        results = []
        for ball, colour in queries:
            # If ball is currently coloured, remove colour
            if ball in balls:
                previous = balls[ball]
                colours[previous] -= 1
                if not colours[previous]:
                    distincts -= 1

            # And colour ball
            balls[ball] = colour
            if not colours[colour]:
                distincts += 1
            colours[colour] += 1

            # And add current distinct colour count to results
            results.append(distincts)
        
        # Finally, return results
        return results
