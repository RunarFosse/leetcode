# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Using segment tree

        # Define the largest possible x-coordinate of a block
        limit = int(5 * 1e4) + 1

        # Store every added obstacle in a sorted list, bounded to be on [1, limit]
        obstacles = SortedList([0, limit])

        # Create a segment tree holding largest available gap ending at an obstacle,
        # within a certain interval
        self.segments = [0] * (4 * (limit + 1))

        # Initially, the whole number line is a gap, ending at the largest x coordinate
        self.update(1, 0, limit, limit, limit)

        # Finally, iterate the queries
        results = []
        for query in queries:
            # If we have a type 1
            if query[0] == 1:
                # Get the intended x-position of the obstacle
                x = query[1]

                # Find the first obstacle to the left, and to the right
                index = obstacles.bisect_right(x)
                left, right = obstacles[index - 1], obstacles[index]

                # And add it to the list
                obstacles.add(x)

                # And update available gaps with the new block in place
                self.update(1, 0, limit, x, x - left)
                self.update(1, 0, limit, right, right - x)
                continue
            
            # Otherwise we have a type 2
            x, size = query[1:]
            
            # Check if there is an available gap for this block in the interval [1, x]
            segment_gap = self.query(1, 0, limit, 0, x)

            # If there is not a obstacle at x, the largest gap might not be represented
            # in the segment tree, so compute this suffix gap with the last obstacle
            index = obstacles.bisect_right(x)
            left = obstacles[index - 1]
            suffix_gap = x - left

            # The result is true if the size fits the largest available gap
            result = max(segment_gap, suffix_gap) >= size
            results.append(result)
    
        # Finally, return the query results
        return results

    def update(self, node: int, left: int, right: int, index: int, value: int) -> None:
        # Set the value at index within the segment tree

        # If the interval is a singleton
        if left == right:
            # We can set the value directly
            self.segments[node] = value
            return
        
        # Otherwise, traverse until we find the child interval containing index
        pivot = (left + right) // 2
        if index <= pivot:
            self.update(node * 2, left, pivot, index, value)
        else:
            self.update(node * 2 + 1, pivot + 1, right, index, value)
        
        # Then update the current value to represent that of its children
        self.segments[node] = max(self.segments[node * 2], self.segments[node * 2 + 1])
    
    def query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> int:
        # Query the value of a range within the segment tree

        # If the current and query intervals are disjoint
        if left > query_right or right < query_left:
            # Then there is no available gap
            return 0
        
        # However, if the current interval is fully within the query interval
        if left >= query_left and right <= query_right:
            # Then return the available gap
            return self.segments[node]
        
        # Otherwise, compute the largest available gap in both children intervals
        pivot = (left + right) // 2
        max_left = self.query(node * 2, left, pivot, query_left, query_right)
        max_right = self.query(node * 2 + 1, pivot + 1, right, query_left, query_right)

        # And return the maximum
        return max(max_left, max_right)
