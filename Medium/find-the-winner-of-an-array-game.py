# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        current, win_count = arr[0], 0
        for i in range(1, len(arr)):
            num = arr[i]

            if num < current:
                win_count += 1
            else:
                current = num
                win_count = 1
            
            if win_count == k:
                break
        
        return current

    

# Iterate array and check if a number n = arr[i] remains maximum
# on the subarray arr[i]-arr[i+k-1]. Then this will be our winner.

# Note, for i = 0 the subarray has to be extended to arr[i]-arr[i+k], as
# this number starts with win_count = 0 (contrary to the others with win_count = 1)

# Now, we also know if we've passed a smaller number within arr[i]-arr[i+k-1], then
# reach a higher number arr[i+j], we can continue iterating from this index i+j, as
# no other number within the interval arr[i]-arr[i+j] possibly can win.