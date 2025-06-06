# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def robotWithString(self, s: str) -> str:
        # Using greedy

        # First, count the frequency of every letter in s
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Then, iterate the string again
        pointer = 0
        t, string = [], []
        for c in s:
            # Append the letter from s to t, and decrement its frequency
            t.append(c)
            frequencies[indexOf(c)] -= 1

            # Keep the pointer located on the smallest lexicographical character in s
            while pointer < 26 and not frequencies[pointer]:
                pointer += 1
            
            # If the letter at the end of t is smaller than this, add it to the string
            while t and indexOf(t[-1]) <= pointer:
                string.append(t.pop())

        # Finally, return this string
        return "".join(string)