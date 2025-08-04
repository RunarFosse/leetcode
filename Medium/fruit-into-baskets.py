# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Using sliding window
        n = len(fruits)

        # First, condense homogeneous subarrays into a single value
        condensed, fruit, count = [], fruits[0], 0
        for i in range(n):
            if fruits[i] != fruit:
                condensed.append((fruit, count))
                count = 0
            fruit = fruits[i]
            count += 1
        condensed.append((fruit, count))

        # Then, slide a window over the condensed fruit trees, counting maximum
        harvested, maximum = 0, 0
        start, end, uniques, fruits = 0, 0, 0, [0] * n
        while end < len(condensed):
            # Extend the window
            fruit, count = condensed[end]
            if not fruits[fruit]:
                uniques += 1
            fruits[fruit] += 1
            harvested += count
            end += 1

            # Shrink the window if containing more than 2 fruits
            while uniques > 2:
                fruit, count = condensed[start]
                harvested -= count
                fruits[fruit] -= 1
                if not fruits[fruit]:
                    uniques -= 1
                start += 1
            
            # And store the maximum harvested number of fruits
            maximum = max(harvested, maximum)
    
        # Finally, return the maximum harvested fruits
        return maximum
