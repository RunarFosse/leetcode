class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapify(self.heap)

        # Add all numbers to the min-heap, where current top element
        # is the k'th largest element in the whole stream
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add value to heap if heap contains less than k elements, or
        # if greater than the current k'th largest
        if len(self.heap) < self.k or val > self.heap[0]:
            heappush(self.heap, val)
        
        # If heap now contains more than k elements, pop the smallest
        if len(self.heap) > self.k:
            heappop(self.heap)

        # K'th largest element is now the root of the heap
        return self.heap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)