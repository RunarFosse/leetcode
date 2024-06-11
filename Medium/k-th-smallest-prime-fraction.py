# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Using binary search
        n = len(arr)

        # Binary search a fraction between 0 and 1 such that
        # there are (k-1) fractions less than the pivot
        left, right = 0, 1
        while left < right:
            pivot = (left+right) / 2
            result = [0, 1]

            # For each element in the array, count the number of fractions
            # which are lower than pivot
            count, pointer = 0, 0
            for num in arr:
                while pointer < n and pivot < num / arr[pointer]:
                    pointer += 1
                count += (n - pointer)
                
                # Early break criteria
                if pointer == n:
                    break

                # Store current biggest fraction less than pivot
                if result[0] / result[1] < num / arr[pointer]:
                    result = [num, arr[pointer]]

            # Move left/right pointer based on fractions lower than pivot
            if count < k:
                left = pivot
            elif count > k:
                right = pivot
            else:
                return result