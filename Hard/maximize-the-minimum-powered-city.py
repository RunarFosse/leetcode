# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(r)

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # Using binary search
        self.stations, self.n = stations, len(stations)

        # Binary search the maximum minimum power of all cities
        left, right = 0, int(10e10)
        while left < right:
            pivot = (left + right) // 2
            if self.canPower(pivot, r, k):
                left = pivot + 1
            else:
                right = pivot
        
        # And return the maximum minimum possible city power
        return left - 1
    
    def canPower(self, x: int, r: int, k: int) -> bool:
        # Iterate all the stations, computing their total power
        power, extensions = sum(self.stations[:min(r, self.n)]), deque([])
        for i in range(self.n):
            if extensions and extensions[0][0] < i - r:
                power -= extensions.popleft()[1]
            if i - r > 0:
                power -= self.stations[i - r - 1]
            if i + r < self.n:
                power += self.stations[i + r]
            
            # And greedily upping it to match the current threshold
            if power < x:
                difference = x - power
                k -= difference
                power += difference
                extensions.append((i + r, difference))
            
            # If we do not have enough extra power stations, return False
            if k < 0:
                return False
        
        # Otherwise, return True
        return True
    