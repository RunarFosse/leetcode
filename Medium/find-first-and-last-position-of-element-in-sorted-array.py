# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Using Binary search
        left, right = 0, len(nums) - 1
        start, end = -1, -1

        if not nums:
            return [start, end]

        while abs(left - right) > 1:
            pivot = (left + right) // 2
            if nums[pivot] < target:
                left = pivot
            elif nums[pivot] > target:
                right = pivot
            else: 
                # If target is found, binary search start and end
                start_l, start_r = left, pivot
                end_l, end_r = pivot, right
                while True:
                    s_pivot = (start_l + start_r) // 2

                    if nums[s_pivot] < target:
                        start_l = s_pivot
                    else:
                        start_r = s_pivot
                    
                    if abs(start_l - start_r) <= 1:
                        break
                
                while True:
                    e_pivot = ceil((end_l + end_r) / 2)

                    if nums[e_pivot] == target:
                        end_l = e_pivot
                    else:
                        end_r = e_pivot

                    if abs(end_l - end_r) <= 1:
                        break
                
                start = start_l if nums[start_l] == target else start_r
                end = end_r if nums[end_r] == target else end_l
                return [start, end]
        
        # If target was not found through binary search 
        # (left and right pointers next to eachother)
        # then manually calculate start and end
        if nums[left] == target:
            start = left
            end = left
        if nums[right] == target:
            end = right
            if start == -1:
                start = right

        return [start, end]
