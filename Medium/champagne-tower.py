# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Using dynamic programming
        opt = [poured]

        # Iterate every row downwards
        for i in range(query_row):
            # Store next row in a new array
            new = [0] * (i + 2)

            # At every row, iterate every glass
            for j in range(i + 1):
                # If the current glass is overflowing
                if opt[j] > 1:
                    # Compute the overflow to both sides
                    excess = (opt[j] - 1) / 2
                    
                    # And pour downwards
                    new[j] += excess
                    new[j + 1] += excess
            
            # Then replace the current row
            opt = new
        
        # Finally, return the amount in the queried glass
        return min(opt[query_glass], 1)


# opt(i, j) - How full the jth glass on the ith row after pouring over.
