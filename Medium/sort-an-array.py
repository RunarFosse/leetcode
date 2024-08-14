# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Using merge sort
        return self.mergesort(nums, 0, len(nums))
    
    def mergesort(self, nums: List[int], start: int, end: int) -> List[int]:
        # If subarray contains at most one element, return it
        if end - start <= 1:
            return nums[start:end]
        
        # Split the current subarray, sorting both sides separately
        middle = (start + end) // 2
        left = deque(self.mergesort(nums, start, middle))
        right = deque(self.mergesort(nums, middle, end))

        # Merge the two sides and return it
        current = []
        for _ in range(start, end):
            if not right or left and left[0] < right[0]:
                current.append(left.popleft())
            else:
                current.append(right.popleft())
    
        return current
