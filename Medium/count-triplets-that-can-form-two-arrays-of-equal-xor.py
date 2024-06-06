# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Using prefix XOR
        prefixes = [0] + arr
        n = len(prefixes)

        # First calculate prefix XOR
        for i in range(1, n):
            prefixes[i] ^= prefixes[i-1]
        
        # Then we need to store previous occurences of XOR values
        # as well as storing previously counted triplets
        occurences = defaultdict(int)
        previous = defaultdict(int)

        # Finally, count triplets
        triplets = 0
        for i in range(n):
            current = prefixes[i]
            triplets += occurences[current] * (i-1) - previous[current]

            # Increment occurences and how many more we've counted
            occurences[current] += 1
            previous[current] += i
        
        # Return total number of triplets we can create
        return triplets