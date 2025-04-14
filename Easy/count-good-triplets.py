# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(1)

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        # Brute force over the three constraints
        good = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # If the first doesn't hold, drop iteration early
                if abs(arr[i] - arr[j]) > a:
                    continue
                
                # Otherwise, iterate k and check the others
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        good += 1
        
        # Finally return the number of good triplets
        return good