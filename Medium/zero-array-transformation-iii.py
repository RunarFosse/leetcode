# Author: Runar Fosse
# Time complexity: O(mlog m + n)
# Space complexity: O(m + n)

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Using greedy
        n = len(nums)

        # Sort the queries in order of increasing start index
        queries = deque(sorted(queries))
        
        # Keep track of current number of decrements using a difference array
        decrements, differences = 0, [0] * (n + 1)

        # Iterate every element in nums
        removals = []
        for i in range(n):
            # Deduce the number of current decrements from the difference array
            decrements += differences[i]

            # And extract all usable removal intervals
            while queries and queries[0][0] <= i:
                # Adding the end index to a max-heap
                _, right = queries.popleft()
                heappush(removals, -right)

            # While the current number is non-zero, use a query to decrement
            while decrements < nums[i]:
                if not removals or -removals[0] < i:
                    # If we have no more removal-queries, nums cannot become a zero array
                    return -1
                
                # Otherwise, count a decrement from the query
                right_neg = heappop(removals)
                decrements += 1
                differences[-right_neg + 1] -= 1
        
        # Finally, return the number of unused removals
        return len(removals)
