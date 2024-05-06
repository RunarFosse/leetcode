# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Using greedy
        n = len(people)

        # Sort in descending order
        people.sort(reverse=True)

        # Using two pointers, count boats needed with greedy approach
        boats = 0
        p1, p2 = 0, n-1
        while p1 <= p2:
            # Check if both can fit in a boat
            if people[p1] + people[p2] <= limit:
                # If so, we can add the lighest person
                p2 -= 1
            
            # The heaviest person goes in a boat either way
            p1 += 1
            boats += 1
        
        # Return the minimum number of boats needed
        return boats


# As a boat can only carry at most two people at the same time, we can
# solve this greedily by always filling the next free boat with the
# current heaviest person.