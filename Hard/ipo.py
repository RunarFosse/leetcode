# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Using greedy
        n = len(profits)

        # First sort profits and capital based on order of decreasing capital
        indices = sorted(range(n), key=lambda i: capital[i], reverse=True)
        profits = [profits[i] for i in indices]
        capital = [capital[i] for i in indices]
        
        # Then pop and add all projects we can do to a max heap
        queue = []
        while capital and capital[-1] <= w:
            queue.append((-profits.pop(), capital.pop()))
        heapify(queue)

        # Then iteratively pick the best project
        while queue and k:
            w += -heappop(queue)[0]
            k -= 1

            # As our capital has (maybe) increased, add new feasible projects
            while capital and capital[-1] <= w:
                heappush(queue, (-profits.pop(), capital.pop()))
            
        # Return our final capital
        return w

# Our strategy should be to greedily pick the project with highest pure profit
# given that we have enough capital to start it.