# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Using combinatorics

        # There are 3 * 2^(n - 1) valid happy strings
        if k > 3 << (n - 1):
            # If k is larger, return empty string
            return ""
        
        # Otherwise, construct the string
        string = [""]
        for i in range(n):
            for c in "abc":
                if c == string[-1]:
                    continue

                # Check which character k corresponds to, and add that
                if k <= 1 << (n - 1 - i):
                    string.append(c)
                    break
                
                # If not, decrement k accordingly
                k -= 1 << (n - 1 - i)
        
        # Finally, return the string
        return "".join(string)
        