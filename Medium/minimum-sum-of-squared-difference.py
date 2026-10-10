# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Using greedy
        n = len(nums1)

        # First, compute the absolute difference of each index, sorted in descending order
        differences = sorted([abs(n1 - n2) for n1, n2 in zip(nums1, nums2)], reverse=True)

        # Work with a global k, instead of two separate k1 and k2.
        k = k1 + k2

        # Then, iterate the differences
        differences.append(0)
        for i in range(n):
            # Compute the number of decrements needed to make all prior
            # differences equal to the next one
            decrements = (differences[i] - differences[i + 1]) * (i + 1)

            # If we have enough remaining differences for this, use them
            if decrements <= k:
                k -= decrements
                continue
            
            # Otherwise, compute how many decrements we actually can use per difference
            decrement, remaining = divmod(k, i + 1)

            # From this, we can compute the largest elements in the seen subset
            largest = differences[i] - decrement

            # Computing the resulting sum of squared differences, and returning it
            total = largest * largest * (i + 1 - remaining)
            total += (largest - 1) * (largest - 1) * remaining
            total += sum(difference * difference for difference in differences[i + 1:])
            return total
        
        # If the loop terminates, then every difference has been set to zero
        return 0


# Because we can make negative numbers, we can combine k1 and k2 into a global k,
# working on the absolute difference instead of each separate number.