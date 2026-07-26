# Author: Runar Fosse
# Time complexity: O(mlog n + n)
# Space complexity: O(m + n)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Using binary search
        m, n = len(queries), len(heights)

        # Iterate all the queries
        answer, deferred = [-1] * m, [[] for _ in range(n)]
        for index, (a, b) in enumerate(queries):
            # If Alice and Bob can meet on the right building
            left, right = min(a, b), max(a, b)
            if left == right or heights[left] < heights[right]:
                # Do so
                answer[index] = right
                continue
            
            # Otherwise, add query as deferred
            deferred[right].append((heights[left], index))
        
        # To compute all deferred queries, iterate buildings from right-to-left
        stack = []
        for i in reversed(range(n)):
            # Solve all queries with current as right building
            for height, index in deferred[i]:
                # By binary searching first occuring building both can jump to
                building = bisect_left(stack, -height, key=lambda e: -heights[e]) - 1
                if building != -1:
                    answer[index] = stack[building]
            
            # And expand and maintain the decreasing monotonic stack
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        
        # Finally, return the answer to each of the queries
        return answer
