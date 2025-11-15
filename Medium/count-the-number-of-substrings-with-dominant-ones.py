# Author: Runar Fosse
# Time complexity: O(n sqrt(n))
# Space complexity: O(n)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Using prefix sum
        n = len(s)

        # Store the index of the previously occuring zero
        previous = [-1] * (n + 1)
        for i in range(n):
            previous[i + 1] = i if s[i] == "0" else previous[i]
        
        # Then slide a window over the string
        dominants = 0
        for end in range(n):
            start, zeros = end, 1 if s[end] == "0" else 0
            while start >= 0 and zeros * zeros <= end:
                # Compute how many ones there are in this current window
                ones = end - previous[start] - zeros

                # If we have dominant ones, compute how many new substrings there are
                if zeros * zeros <= ones:
                    dominants += min(ones - zeros * zeros + 1, start - previous[start])
                
                # And expand the window until the previous zero
                start = previous[start]
                zeros += 1

        # Finally, return the number of substrings with dominant ones
        return dominants
        