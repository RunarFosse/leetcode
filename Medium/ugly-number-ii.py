# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Using greedy
        uglies = [1]

        # Store the index of which the next ugly number per multiple
        # should be calculated from
        index2, index3, index5 = 0, 0, 0

        # Greedily calculate every ugly number up until the n'th
        for _ in range(1, n):
            # Calculate the three possible next ugly numbers
            possibles = 2*uglies[index2], 3*uglies[index3], 5*uglies[index5]
            next_ugly = min(possibles)

            # Increment the indices pointing to the next ugly number
            if possibles[0] == next_ugly:
                index2 += 1
            if possibles[1] == next_ugly:
                index3 += 1
            if possibles[2] == next_ugly:
                index5 += 1
            
            # And append it
            uglies.append(next_ugly)
            
        # And finally return the last ugly number calculated
        return uglies[-1]