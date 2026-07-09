# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Using greedy

        # First, preprocess every connected component
        components, current = [0] * n, 0
        for i in range(1, n):
            # Check the difference between neighbour nodes
            if nums[i] - nums[i - 1] > maxDiff:
                # If they are too large, the nodes belong to separate components
                current += 1
            components[i] = current 

        # Then, iterate every query
        answer = []
        for u, v in queries:
            # Checking if they belong to the same connected component
            answer.append(components[u] == components[v])

        # Finally, return all query answers
        return answer
