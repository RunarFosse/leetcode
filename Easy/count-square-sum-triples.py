# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def countTriples(self, n: int) -> int:
        # Precompute square numbers to optimize later search
        squares = set([i * i for i in range(1, n + 1)])
        
        # Then iterate values for a and b
        triples = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Check if c^2 is a square, and count it if so
                c2 = a * a + b * b
                if c2 in squares:
                    triples += 1
        
        # Finally, return the number of square sum triples
        return triples
