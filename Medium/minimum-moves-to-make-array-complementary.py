# Author: Runar Fosse
# Time complexity: O(n + m)
# Space complexity: O(m)

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Iterate the number pairs
        targets = [0] * (2 * limit + 2)
        for i in range(n // 2):
            left, right = nums[i], nums[n - 1 - i]

            # If we set both elements to 1, we spend 2 moves
            targets[2] += 2

            # If we only need to set 1 element, we only spend 1 move
            targets[min(left, right) + 1] -= 1

            # If we change no elements, we spend no moves
            targets[left + right] -= 1

            # However, afterwards we spend 1 move
            targets[left + right + 1] += 1

            # If we exceed the maximum + limit, we must spend 2 moves
            targets[max(left, right) + limit + 1] += 1
        
        # Finally, iterate through the end targets
        prefix, minimum = 0, n
        for i in range(2, 2 * limit + 1):
            # Storing the minimum number of moves to make nums complementary
            prefix += targets[i]
            minimum = min(prefix, minimum)
        
        # Finally, return this minimum number of moves
        return minimum
