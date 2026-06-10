# Author: Runar Fosse
# Time complexity: O((n + k)log n)
# Space complexity: O(n)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Using segment tree
        n = len(nums)
        
        # Build a maximum and minimium segment tree out of the array
        maximum = SegmentTree(nums, max)
        minimum = SegmentTree(nums, min)

        # Declare a helper function to easily compute the value of a subarray
        subarray_value = lambda left, right: (
            maximum.query(1, 0, n - 1, left, right) - 
            minimum.query(1, 0, n - 1, left, right)
        )

        # Add all subarray values starting at index 0 to a max heap
        heap = [(-subarray_value(0, right), 0, right) for right in range(n)]
        heapify(heap)

        # Then, greedily pick the k most valuable subarrays
        total = 0
        while k:
            negated, left, right = heappop(heap)
            total += -negated
            k -= 1

            # If the current subarray is not a singleton
            if left != right:
                # Add a smaller partition back into the heap
                heappush(heap, (-subarray_value(left + 1, right), left + 1, right))
        
        # Finally, return the maximum total subarray value
        return total

class SegmentTree:
    def __init__(self, nums: List[int], comparator: Callable[[int, int], int]):
        # Declare a comparator segment tree from nums
        n = len(nums)
        self.comparator = comparator
        self.tree = [0] * (4 * n)
        self.build(1, 0, n - 1, nums)
    
    def build(self, node: int, left: int, right: int, nums: List[int]) -> None:
        # If the interval is a singleton, set a leaf value
        if left == right:
            self.tree[node] = nums[left]
            return
        
        # Otherwise, split and recurse
        pivot = (left + right) // 2
        self.build(node * 2, left, pivot, nums)
        self.build(node * 2 + 1, pivot + 1, right, nums)

        # And set current node as the comparative result of both children
        self.tree[node] = self.comparator(self.tree[node * 2], self.tree[node * 2 + 1])
    
    def query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> int:
        # If the query range covers the whole current range
        if query_left <= left and right <= query_right:
            # Return this consolidated parent value
            return self.tree[node]
        
        # Otherwise, split and recurse
        pivot = (left + right) // 2
        children = []
        if query_left <= pivot:
            children.append(self.query(node * 2, left, pivot, query_left, query_right))
        if query_right > pivot:
            children.append(self.query(node * 2 + 1, pivot + 1, right, query_left, query_right))
        
        # If there is only one child within the query interval, return it
        if len(children) == 1:
            return children[0]
        
        # Otherwise return the comparative result
        return self.comparator(children[0], children[1])
