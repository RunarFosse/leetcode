# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Using prefix sum
        n = len(customers)

        # Calculate missed customers, and add non-missed to result
        satisfied = 0
        prefixes = [0]
        for i in range(n):
            prefixes.append(prefixes[-1])
            if grumpy[i]:
                prefixes[-1] += customers[i]
            else:
                satisfied += customers[i]
        
        # Then find the biggest window of missed customers
        max_missed = 0
        for i in range(n):
            if i+minutes > n:
                break
            missed = prefixes[i+minutes] - prefixes[i]
            max_missed = max(missed, max_missed)
        
        # Return satisfied + maximum missed customers
        return satisfied + max_missed


# We need to find a window of size minutes containing the maximum number
# of customers missed by the owner being grumpy. This we add to the customers
# not missed and return.