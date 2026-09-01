# Author: Runar Fosse
# Time complexity: O(mnk2^l)
# Space complexity: O(mnk2^l)

# where l is the amount of litter in the classroom

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # Using BFS
        m, n = len(classroom), len(classroom[0])

        # First, iterate the classroom, finding the start, and give each litter an id
        start, current, litter = None, 0, {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    litter[(i, j)] = current
                    current += 1
        
        # Then, perform BFS over the state space
        queue, seen = deque([(start, (1 << current) - 1, energy + 1, 0)]), defaultdict(int)
        while queue:
            # Unpack the current state
            (i, j), remaining, stamina, steps = queue.popleft()

            # If we are out of energy, we stop
            if stamina == 0:
                continue

            # Otherwise decrement current energy count
            stamina -= 1

            # Check the current cell state
            match classroom[i][j]:
                case "L":
                    # If it is litter, pick it up
                    remaining &= ~(1 << litter[(i, j)])
                case "R":
                    # If it is a energy recharge, recharge
                    stamina = energy
            
            # If this results in us picking up all the litter
            if remaining == 0:
                # Return the step count
                return steps
            
            # Then move on to the neighbours
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # If inside and neighbour cell is not an obstacle
                if 0 <= i + a < m and 0 <= j + b < n and classroom[i + a][j + b] != "X":
                    state = ((i + a, j + b), remaining)
                    # And we have not visited that state before, with more energy
                    if seen[state] < stamina:
                        queue.append((*state, stamina, steps + 1))
                        seen[state] = stamina

        # If it is impossible to pick up all the litter, return -1
        return -1
