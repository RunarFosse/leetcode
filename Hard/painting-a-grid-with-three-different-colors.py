# Author: Runar Fosse
# Time complexity: O(m4^m + n3^m)
# Space complexity: O(3^m)

class Solution:
    mod = int(1e9 + 7)
    def colorTheGrid(self, m: int, n: int) -> int:
        # Using dynamic programming

        # First, precompute the number of validly colored states
        valids, states = {}, 0
        for bits in range(pow(3, m)):
            colors, valid = [None] * m, True
            for i in range(m):
                colors[i] = bits % 3
                bits //= 3

                # If any color matches the previous
                if i > 0 and colors[i] == colors[i - 1]:
                    # The current column is invalid
                    valid = False
                    break
            
            # Store each valid column coloring, with a corresponding index
            if valid:
                valids[tuple(colors)] = states
                states += 1
        
        # Then, compute every valid neighbour state and create a state space graph
        adjls = [[] for _ in range(states)]
        for state1, index1 in valids.items():
            for state2, index2 in valids.items():
                # If no horizontal color is identical
                if not any(color1 == color2 for color1, color2 in zip(state1, state2)):
                    # Then these states are valid neighbours
                    adjls[index1].append(index2)
        
        # Finally, compute the DP array
        opt = [1] * states
        for _ in range(n - 1):
            temp = [0] * states
            for state in valids.values():
                temp[state] = sum(opt[neighbour] for neighbour in adjls[state]) % self.mod
            opt = temp
        
        # And return the total number of grid colorings with three different colors
        return sum(opt) % self.mod


# By storing valid colored columns as a state, we can create a state space graph
# by connecting each state with each other valid neighbour state, greatly simplifying
# our DP.

# opt(i, state) - The number of different valid grid colorings we can have by appending
#                 the next valid colored column 'state' to a grid of i columns.

# Base case:
# opt(0, _) = 1

# Recurrency:
# opt(i, state) = sum(opt(i - 1, neighbour) for neighbour in adjls[state])

# No. states = n * states = n * (3 * 2^(m-1))
# Time complexity per state -> O(3^m)
# Total time complexity => O(n3^m)

# Adding precomputation of state space graph, with time complexity of O(m4^m),
# the resulting time complexity ends up being O(m4^m + n3^m)