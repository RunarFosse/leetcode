# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Here, n denotes the order of a + b + c, and we have that 3n >= a + b + c.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Using greedy
        string = []

        # Iterate the longest possible string
        curr_a = curr_b = curr_c = 0
        for _ in range(a + b + c):
            # Add an 'a' if it is maximum, or if we cannot add others
            if (a >= b and a >= c and curr_a < 2) or (a > 0 and (curr_b == 2 or curr_c == 2)):
                string.append("a")
                a -= 1
                curr_a += 1
                curr_b = curr_c = 0
            
            # Add a 'b' if it is maximum, or if we cannot add others
            elif (b >= a and b >= c and curr_b < 2) or (b > 0 and (curr_a == 2 or curr_c == 2)):
                string.append("b")
                b -= 1
                curr_b += 1
                curr_a = curr_c = 0

            # Add a 'c' if it is maximum, or if we cannot add others
            elif (c >= a and c >= b and curr_c < 2) or (c > 0 and (curr_a == 2 or curr_b == 2)):
                string.append("c")
                c -= 1
                curr_c += 1
                curr_a = curr_b = 0
        
        # Finally, return the string
        return "".join(string)