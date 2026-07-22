# Author: Runar Fosse
# Time complexity: O(mlog n + n)
# Space complexity: O(m + n)

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        # Using segment tree
        m, n = len(queries), len(s)

        # First, compute the consecutive '0' blocks, as well as total number of '1's
        blocks, ones = [], 0
        for i in range(n):
            # If we have a '1'
            if s[i] == '1':
                # Increment counter
                ones += 1
                continue
            
            # If we instead have a '0', either continue block or create a new
            if blocks and blocks[-1][2] == i - 1:
                blocks[-1][0] += 1
                blocks[-1][2] += 1
            else:
                blocks.append([1, i, i])
        
        # If there are less then two '0' blocks, we cannot make any trade in any query
        if len(blocks) < 2:
            return [ones] * m

        # However if we can, store cumulative length of every adjacent '0' block
        adjacent = [block1[0] + block2[0] for block1, block2 in pairwise(blocks)]
        
        # From all these adjacent blocks, construct a maximum segment tree
        maximum = SegmentTree(adjacent)

        # Then, iterate all the queries
        answer = []
        for left, right in queries:
            # Find the consecutive '0' blocks intersecting left and right
            i = bisect_left(blocks, left, key=lambda e: e[2])
            j = bisect_right(blocks, right, key=lambda e: e[1]) - 1

            # If they are pointing to the same block, or no block at all
            if i >= j or i >= len(blocks) or j < 0:
                # Then we cannot make a trade
                answer.append(ones)
                continue

            # Compute each of the block intersections
            left_zeros = blocks[i][2] - max(left, blocks[i][1]) + 1
            right_zeros = min(right, blocks[j][2]) - blocks[j][1] + 1
            
            # If they are pointing to two adjacent blocks
            if i + 1 == j:
                # We can only make one trade
                answer.append(left_zeros + right_zeros + ones)
                continue
            
            # Otherwise, make the best trade between any block inside the query interval
            trade1 = left_zeros + blocks[i + 1][0]
            trade2 = blocks[j - 1][0] + right_zeros

            # Querying the maximum segment tree to maximize full blocks within interval
            trade3 = maximum.query(i + 1, j - 2)

            answer.append(max(trade1, trade2, trade3) + ones)
        
        # Finally, return the best trade for each query
        return answer

class SegmentTree:
    def __init__(self, array: List[int]):
        self.length = len(array)
        self.array = array
        self.tree = [0] * (4 * self.length)
        self.build(1, 0, self.length - 1)
    
    def build(self, node: int, left: int, right: int) -> None:
        # If interval is singleton
        if left == right:
            # Set the source value of the tree
            self.tree[node] = self.array[left]
            return
        
        # If not, find the pivot and recurse downwards
        pivot = (left + right) // 2
        self.build(node << 1, left, pivot)
        self.build((node << 1) + 1, pivot + 1, right)

        # Setting the current segment tree value to the maximum
        self.tree[node] = max(self.tree[node << 1], self.tree[(node << 1) + 1])
    
    def query(self, query_left: int, query_right: int) -> int:
        # If query interval is invalid, it contains nothing
        if query_left > query_right:
            return 0
        
        # Otherwise, return the queried information
        return self._query(1, 0, self.length - 1, query_left, query_right)
    
    def _query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> int:
        # If current interval is fully inside query interval, return early
        if left >= query_left and right <= query_right:
            return self.tree[node]
        
        # Otherwise, split the search interval and recurse
        pivot = (left + right) // 2
        children = []
        if query_left <= pivot:
            children.append(self._query(node << 1, left, pivot, query_left, query_right))
        if query_right > pivot:
            children.append(self._query((node << 1) + 1, pivot + 1, right, query_left, query_right))

        # Returning the maximum
        return max(children, default=0)
