# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Simulate the chef handling every customer, storing current
        # time and calculating running average
        time, average_wait = 0, 0
        for i, (arrival, length) in enumerate(customers):
            # Wait until customer arrives, and cook
            time = max(arrival, time) + length

            # Add to average wait time
            wait = time - arrival
            average_wait += (wait - average_wait) / (i+1)
    
        # Return average wait time
        return average_wait