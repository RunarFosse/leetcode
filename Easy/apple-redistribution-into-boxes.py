# Author: Runar Fosse
# Time complexity: O(mlog m + n)
# Space complexity: O(m)

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Using greedy

        # At first, count the total number of apples
        apples = sum(apple)

        # Sort the boxes in order of decreasing capacity
        capacity.sort(reverse=True)

        # Then iterate the boxes
        boxes = 0
        for box in capacity:
            # Placing apples into them
            apples -= box
            boxes += 1

            # Until every apple has been distributed
            if apples <= 0:
                break
        
        # Finally, return the minimum number of boxes needed
        return boxes
