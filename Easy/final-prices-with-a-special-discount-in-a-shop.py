# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Using monotonic stack
        n = len(prices)

        # Iterate the list from behind
        stack = []
        for i in reversed(range(n)):
            # Pop invalid prices from the stack
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            # Compute discount
            discount = stack[-1] if stack else 0

            # And add original back to stack
            stack.append(prices[i])
            prices[i] -= discount

        # Return the discounted prices
        return prices