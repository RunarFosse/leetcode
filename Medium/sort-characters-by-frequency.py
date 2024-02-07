# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        indexOf = lambda c : ord(c) - ord("0")
        frequencies = [(0, chr(i)) for i in range(ord("0"), ord("z")+1)]

        # Count frequencies in string
        for c in s:
            i = indexOf(c)
            frequencies[i] = (frequencies[i][0] + 1, frequencies[i][1])
        
        # Sort in descending order based on character frequency
        frequencies.sort(key=lambda e : -e[0])

        # Reconstruct the returned string
        return "".join(map(lambda e : e[1] * e[0], frequencies))

        
# Count frequency of characters, sort this frequency array in descending order
# and then reconstruct the new sorted string.

# Time complexity is O(n), as the array we are sorting contains a constant
# number of elements, leading to constant sorting runtime.