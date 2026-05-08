# Author: Runar Fosse
# Time complexity: O(nlog(log(n)))
# Space complexity: O(n)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # Using BFS
        n = len(nums)

        # Iterate the array, finding the maximum entry, and indices of all elements
        indices, maximum = defaultdict(list), 0
        for i in range(n):
            indices[nums[i]].append(i)
            maximum = max(nums[i], maximum)

        # Then, compute every prime number up to this maximum
        is_prime = [False, False] + [True] * (maximum - 1)
        for i in range(2, maximum + 1):
            if not is_prime[i]:
                continue
            for j in range(2 * i, maximum + 1, i):
                is_prime[j] = False

        # Finally, perform BFS
        queue, seen = deque([(0, 0)]), set()
        while queue:
            i, distance = queue.popleft()
            if i in seen:
                continue
            seen.add(i)
            
            # If we are at the end, return the minimum distance
            if i == n - 1:
                return distance
            
            # Add valid adjacent steps to queue
            if i > 0:
                queue.append((i - 1, distance + 1))
            queue.append((i + 1, distance + 1))

            # If the current indexed number is prime
            if is_prime[nums[i]]:
                # Add prime teleportation neighbours to queue
                for multiple in range(nums[i], maximum + 1, nums[i]):
                    for neighbour in indices[multiple]:
                        queue.append((neighbour, distance + 1))

                    # Optimize by removing visited neighbours
                    indices[multiple].clear()
