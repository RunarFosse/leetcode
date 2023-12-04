# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Using sliding window
        max_good = None

        p1 = p2 = 0
        while p2 < len(num):
            # If first and last number in window is equal
            if num[p1] == num[p2]:
                # And the window has size 3
                if p2 - p1 == 2:
                    # Store maximum max_good
                    unique_number = int(num[p1])
                    if max_good == None:
                        max_good = unique_number
                    else:
                        max_good = max(unique_number, max_good)
                    # Move first pointer
                    p1 += 1
                # If not, move second pointer
                else:
                    p2 += 1
            # If not, move first pointer (and possible second)
            else:
                p1 += 1
                if p2 < p1:
                    p2 = p1

        # If no good integer, return empty string
        if max_good == None:
            return ""
        
        # Return string of largest good integer
        return str(max_good) * 3

        
# Find substring containing only 1 digit, and store the largest digit fulfilling this
# Then we have your largestGoodInteger.