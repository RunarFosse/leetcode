# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Using two pointer approach
        n = len(nums)

        nums.sort()
        triplets = []
        for i in range(n):
            # If current number is bigger than 0, prematurely exit loop
            if nums[i] > 0:
                break
            # First number needs to be unique from last iteration
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1
            while j < k:
                triplet = [nums[i], nums[j], nums[k]]
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplets.append(triplet)

                    # Update the window, keeping the second number
                    # also unique from last iteration
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                
                # If not, shrink the window based on the sum size
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
                
        return triplets
