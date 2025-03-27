# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        # First, find the majority element
        temporary, count = nums[0], 0
        for num in nums:
            if num == temporary:
                count += 1
            else:
                count -= 1
            
            # If count ever is 0, change temporary x
            if not count:
                temporary = num
                count = 1
        
        # Then, compute actual frequency of x
        x, frequency = temporary, 0
        for num in nums:
            if num == x:
                frequency += 1
        
        # Then, find the smallest index where x is dominant in both subarrays
        xs = 0
        for i in range(n - 1):
            if nums[i] == x:
                xs += 1
            
            # If it is, return current index
            if xs > (i + 1) // 2 and frequency - xs > (n - i - 1) // 2:
                return i

        # If loop terminates, there exist no such index
        return -1
