# Author: Runar Fosse
# Time complexity: O((n+m)log n)
# Space complexity: O(n)

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Using binary search

        # Store start bloom and end bloom times seperately
        starts, ends = [], []
        for [start, end] in flowers:
            starts.append(start)
            ends.append(end + 1) # As flower is blooming while in [starts, ends] add 1
        
        # Sort both in ascending order
        starts.sort()
        ends.sort()

        # For each person, binary search how many have started, and 
        # how many have ended when said person arrives
        # Bloomed at that time is equal to started - ended
        bloomed = []
        for time in people:
            # No bloom if non started or all ended
            if time < starts[0] or time > ends[-1]:
                bloomed.append(0)
                continue
    
            if time >= starts[-1]:
                started = len(starts)
            else:
                started = self.binarySearch(time, starts) + 1

            if time < ends[0]:
                ended = 0
            else:
                ended = self.binarySearch(time, ends) + 1
                
            bloomed.append(started - ended)
        
        return bloomed
    
    def binarySearch(self, value: int, list: List[int]) -> int:
        left, right = 0, len(list) - 1

        while left < right:
            pivot = (left + right) // 2

            if list[pivot] == value:
                # Could have duplicates, so ensure finding last
                while pivot < len(list) and list[pivot] == value:
                    pivot += 1
                return pivot - 1
            
            if left == right - 1:
                break
            
            if list[pivot] < value:
                left = pivot
            else:
                right = pivot
        
        if list[right] <= value:
            return right
        
        return left