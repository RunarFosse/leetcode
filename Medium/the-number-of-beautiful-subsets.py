# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Using greedy
        total = 0
        subsets = defaultdict(int)

        # Sort the numbers array in ascending order, grouped by modulo
        nums.sort(key=lambda x : (x % k, x))

        # For each element in the array
        for num in nums:
            # Add all subsets where no element satisfies element - num == k
            current = total - (subsets[num - k])
            # And add a subset representing the singleton { num }
            current += 1
        
            # Store all computed subset counts
            subsets[num] += current
            total += current

        # And return all beautiful subsets
        return total
